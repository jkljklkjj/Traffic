#include<bits/stdc++.h>
#define int long long
using namespace std;
int a[500100]={0};
signed main(){
    int n,l,r;
    cin>>n>>l>>r;
     
    //int send=r-l;
    //send*m+r=n
//  int ci=n/(r-l);
//  int yu=n%(r-l);
//  int ney=ci*r+yu;
//  if(yu!=0)ney+=ci*l;
    int yu=n;
    int ci=0;
    while(yu>r){
        yu-=(r-l);
        ci++;
    }
    int ney=ci*(r)+ci*l+yu;
    //cout<<ci<<" "<<ney<<endl;
 
     
    long long ey=0;
    for(int i=1;i<=n;i++){
        cin>>a[i];
        if(a[i]%2==0)a[i]--;
        a[i]=min(a[i],2*ci+1);
        ey+=a[i];
    }
    //cout<<ey;
    if(n<l){
        cout<<"No";
        return 0;
    }
    if(ey>=ney)cout<<"Yes";
    else cout<<"No";
    return 0;
}