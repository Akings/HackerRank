#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int n;
    int arr[1000];
    cin >> n;
    for (int i=0; i<=n; ++i){cin >> arr[i];}
    for (int i=n-1; i>=0; --i){cout << arr[i] << " ";}
    return 0;
}
