#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n,q;
    cin>>n>>q;
    vector<vector<int>> arr;
    for (int i=0;i<n;i++){
        int s;
        cin>>s;
        vector<int> vl;
        for (int j=0;j<s;j++){
            cin>>vl[i];
        }
        arr.push_back(vl);
    }
    // int index;int index
    for(int i=0;i<q;i++){
        int in1,in2;
        cin>>in1>>in2;
        cout<<arr[in1][in2];
    }
    return 0;
}