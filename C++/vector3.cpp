#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
/*For each query you have to print "Yes" (without the quotes) if the number is present and at which index(1-based) it is present separated by a space.

If the number is not present you have to print "No" (without the quotes) followed by the index of the next smallest number just greater than that number.

You have to output each query in a new line.*/

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int N;
    cin>>N;
    vector<int> v(N+1);
    for(int i=1;i<v.size();i++){
        cin>>v[i];
    }
    int q;
    cin>>q;
    for(int i=0;i<q;i++){
        int Q,ind;
        cin>>Q;
        ind=distance(v.begin(),find(v.begin(),v.end(),Q));
        // cout<<ind;
        if (ind != v.size()){
           
            cout<<"Yes "<<ind<<endl;
           
        }
        else{
            if (v[ind]==v[v.size()-1]){
                cout<<"Yes "<<ind<<endl;
            }
            else{
                auto it=find_if(v.begin(), v.end(), [Q](int x) { return x > Q; });
                cout<<"No "<<distance(v.begin(),it)<<endl;
            }
        }
    }
    return 0;
}
