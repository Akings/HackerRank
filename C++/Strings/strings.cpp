#include <iostream>
#include <string>
using namespace std;


int main() {
    string first, second;
    char tmp;
    cin >> first;
    cin >> second;
    cout << first.size() << " " << second.size() << endl;
    cout << first + second << endl;
    tmp = first[0];
    first[0] = second[0];
    second[0] = tmp;
    cout << first << " " << second;
    return 0;
}
