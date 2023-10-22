/** 레퍼런스 변수 */
#include <iostream>

using namespace std;

void swap(int &a, int &b){
    int tmp = a;
    a = b;
    b = tmp;
}

int main(){
    int a(5);
    int &p = a;
    /** this meaning is the change of the value of a. */
    p = 10;

    cout << p << endl;
    cout << a << endl;

    int c(5), d(7);
    swap(c, d);

    cout << c << endl;
    cout << d << endl;

    
    int &r1 = a;
    /** the reference value and the pointer doesn't appear as constant.
     * because the value of the constant isn't stored in the cumputer's memory.
     * so two examples below have errors.
    */
    int &r2 = 3;
    int &r3 = a * a;

    /** 
     * the meaning of an r-value is that represents the right-hand side value, and as such, so it cann't be changed.
     * in this case, 'a' is a variable. so it can be changed, and as such, 'a' is l-value.
    */
    int &&r1 = a;
    int &&r2 = 3;
    int &&r3 = a * a;

}