# -*- coding: utf-8 -*-#
# Author: WSKH
# Blog: wskh0929.blog.csdn.net
# Time: 2023/2/13 15:23
# Description:

import time
import random

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号 #有中文出现的情况，需要u'内容'

from EdmonsKarp import Edmons_Karp_Solve
from FordFulkerson import Ford_Fulkerson_Solve
from Dinic import Dinic_Solve
from copy import deepcopy


class Node:
    def __init__(self, name, arc_dict):
        self.name = name
        self.arc_dict = arc_dict


def create_node(name, next_list, flow_list):
    arc_dict = {}
    for i in range(len(next_list)):
        arc_dict[next_list[i]] = flow_list[i]
    return Node(name, arc_dict)


def create_instance(m, n, seed=666):
    random.seed(seed)
    S = "S"
    E = "E"
    node_list = []
    name_index_dict = {}
    name_index_dict["S"] = 0
    name_index_dict["E"] = m + n + 1
    for i in range(m + n):
        name_index_dict[str(i + 1)] = i + 1
    # 构造起点
    node_list.append(create_node("S", [str(i + 1) for i in range(m)], [random.randint(800, 1200) for _ in range(m)]))
    # 构造第一层
    for i in range(m):
        node_list.append(
            create_node(str(i + 1), [str(i + j + 2) for j in range(n)], [random.randint(800, 1200) for _ in range(n)]))
    # 构造第二层
    for i in range(n):
        next_list = ["E"]
        flow_list = [random.randint(800, 1200)]
        for j in range(m):
            next_list.append(str(j + 1))
            flow_list.append(0)
        node_list.append(create_node(str(m + i + 1), next_list, flow_list))

    # 构造终点
    node_list.append(create_node("E", [], []))
    return S, E, node_list, name_index_dict


def test1():
    m = 10
    n_arr = [i for i in range(1, 21, 1)]
    time_dict = {
        "Ford-Fulkerson": [],
        "Edmons-Karp": [],
        "Dinic": []
    }
    for n in n_arr:
        instance = create_instance(m, n)

        S, E, node_list, name_index_dict = deepcopy(instance)
        start_time = time.time()
        Ford_Fulkerson_Solve(S, E, node_list, name_index_dict)
        time_dict["Ford-Fulkerson"].append(time.time() - start_time)

        S, E, node_list, name_index_dict = deepcopy(instance)
        start_time = time.time()
        Edmons_Karp_Solve(S, E, node_list, name_index_dict)
        time_dict["Edmons-Karp"].append(time.time() - start_time)

        S, E, node_list, name_index_dict = deepcopy(instance)
        start_time = time.time()
        Dinic_Solve(S, E, node_list, name_index_dict)
        time_dict["Dinic"].append(time.time() - start_time)
    plot(time_dict, n_arr, "固定m为10，n与运行时间的关系", "n")


def test2():
    n = 10
    m_arr = [i for i in range(1, 21, 1)]
    time_dict = {
        "Ford-Fulkerson": [],
        "Edmons-Karp": [],
        "Dinic": []
    }
    for m in m_arr:
        print(m)
        instance = create_instance(m, n)

        S, E, node_list, name_index_dict = deepcopy(instance)
        start_time = time.time()
        Ford_Fulkerson_Solve(S, E, node_list, name_index_dict)
        time_dict["Ford-Fulkerson"].append(time.time() - start_time)

        S, E, node_list, name_index_dict = deepcopy(instance)
        start_time = time.time()
        Edmons_Karp_Solve(S, E, node_list, name_index_dict)
        time_dict["Edmons-Karp"].append(time.time() - start_time)

        S, E, node_list, name_index_dict = deepcopy(instance)
        start_time = time.time()
        Dinic_Solve(S, E, node_list, name_index_dict)
        time_dict["Dinic"].append(time.time() - start_time)
    plot(time_dict, m_arr, "固定n为10，m与运行时间的关系", "m")


def plot(time_dict, arr, title, x_label):
    for key in time_dict.keys():
        plt.plot(arr, time_dict[key], marker=".", label=key)
    plt.legend()
    plt.xlabel(x_label)
    plt.ylabel("运行时间(s)")
    plt.title(title)
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    # test1()
    test2()

