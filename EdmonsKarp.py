# -*- coding: utf-8 -*-#
# Author: WSKH
# Blog: wskh0929.blog.csdn.net
# Time: 2023/2/13 11:54
# Description: Edmons Karp 算法求解最大流问题

from queue import PriorityQueue


class Node:
    def __init__(self, name, arc_dict):
        self.name = name
        self.arc_dict = arc_dict


class Label:
    def __init__(self, route, last_flow):
        self.route = route
        self.last_flow = last_flow

    def __lt__(self, o):
        if len(self.route) == len(o.route):
            return 0
        else:
            return 1 if len(self.route) > len(o.route) else -1


def create_node(name, next_list, flow_list):
    arc_dict = {}
    for i in range(len(next_list)):
        arc_dict[next_list[i]] = flow_list[i]
    return Node(name, arc_dict)


def Edmons_Karp_Solve(s, e, node_list, name_index_dict):
    '''
    Edmons Karp 算法核心函数
    :param s: 起始节点名称
    :param e: 终止节点名称
    :param node_list: 节点列表
    :param name_index_dict: 节点名字和索引字典
    :return: 返回搜索到的所有增广路径及其流值
    '''
    routes = []
    while True:
        res = bfs(s, e, node_list, name_index_dict)
        if res is None:
            return routes
        # 追加增广路径到routes
        routes.append([res.route, res.last_flow])
        # 更新node_list
        route, flow = res.route, res.last_flow
        for i in range(len(route) - 1):
            n1 = node_list[name_index_dict[route[i]]]
            n2 = node_list[name_index_dict[route[i + 1]]]
            # 正向更新 n1 -> n2 剩余流量减少
            if n2.name in n1.arc_dict.keys() and n1.arc_dict[n2.name] is not None:
                n1.arc_dict[n2.name] = n1.arc_dict[n2.name] - flow
            # 反向更新 n2 -> n1 剩余流量增加
            if n1.name in n2.arc_dict.keys() and n2.arc_dict[n1.name] is not None:
                n2.arc_dict[n1.name] = n2.arc_dict[n1.name] + flow


def bfs(s, e, node_list, name_index_dict):
    queue = PriorityQueue()
    queue.put(Label([s], None))
    while queue.empty() is False:
        res = queue.get()
        index = name_index_dict[res.route[-1]]
        for next_node_name in node_list[index].arc_dict.keys():
            if next_node_name not in res.route:
                flow = node_list[index].arc_dict[next_node_name]
                if flow is None or flow > 0:
                    route = res.route.copy()
                    route.append(next_node_name)
                    if next_node_name == e:
                        return Label(route, min_flow(res.last_flow, flow))
                    queue.put(Label(route, min_flow(res.last_flow, flow)))


def min_flow(f1, f2):
    '''
    求两个流量的较小者
    '''
    if f1 is None:
        return f2
    elif f2 is None:
        return f1
    else:
        return min(f1, f2)


if __name__ == '__main__':
    # 格式: [节点名, 后继节点的名称, 当前节点到各个后继的流量] （None 代表流量无穷大）
    graph = [
        ["S", ["1", "2", "3"], [None, None, None]],
        ["1", ["4"], [1]],
        ["2", ["4", "6"], [1, 1]],
        ["3", ["5"], [1]],
        ["4", ["1", "2", "E"], [0, 0, 1]],
        ["5", ["3", "E"], [0, 1]],
        ["6", ["2", "E"], [0, 1]],
        ["E", [], []]
    ]
    name_index_dict = dict()
    node_list = []
    for i in range(len(graph)):
        node_list.append(create_node(graph[i][0], graph[i][1], graph[i][2]))
        name_index_dict[graph[i][0]] = i

    # 调用算法求解最大流
    routes = Edmons_Karp_Solve("S", "E", node_list, name_index_dict)
    for i, (route, flow) in enumerate(routes):
        print(f"Route-{i + 1}: {route} , flow: {flow}")
