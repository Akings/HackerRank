#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;  // number of variable-length arrays
    int q;  // number of queries
    int k;  // size of array
    int i;  // index in array a
    int j;  // index in the array referenced by a[i]
    vector<vector<int>> arr;  //variable-length array
    vector<vector<int>> queries;
    // Reading n and q
    cin >> n >> q;
    // reading variable-length array
    for (int a=0; a<n; ++a){
        cin >> k;
        vector<int> tmp_vec;
        for (int b=0; b<k; ++b){
            int tmp_int;
            cin >> tmp_int;
            tmp_vec.push_back(tmp_int);
        }
        arr.push_back(tmp_vec);
    }
    // reading queries
    for (int a=0; a<q; ++a){
        vector<int> tmp_vec;
        cin >> i >> j;
        tmp_vec.push_back(i);
        tmp_vec.push_back(j);
        queries.push_back(tmp_vec);
    }
    // displaying elements
    for (auto & query: queries){
        i = query[0];
        j = query[1];
        cout << arr[i][j] << endl;
    }
    return 0;
}
