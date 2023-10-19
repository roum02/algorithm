#include <iostream>

using namespace std;

int main() {
    /** The meaning of the two sentences below is completely identical. 
     * only for initalizing a variable.
    */
    int a(10);
    int b = a;

    cout << a << b << endl;
}