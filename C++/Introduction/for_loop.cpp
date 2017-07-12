#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int a, b;
    string represent[10] = {"null", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    cin >> a >> b;
    for(int i=a; i<=b; ++i){
        if (i<=9){
            cout << represent[i] << endl;
        }
        else {
            (i % 2 == 0) ? cout << "even\n" :  cout << "odd\n";
        }
    }
    return 0;
}
