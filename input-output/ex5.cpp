/** 범위기반 for문 */
#include <iostream>

using namespace std;

int main(){
    int arr[10] = { 3,1,4,1,5,9,2,6,5,3};

    for (int i=0; i<10; i++){
        cout << arr[i] << ' ';
    }

    cout << "-----" << endl;

    /** each value in array is processed using a function that formats it as array[index] */
    for (int n:arr){
        cout << n << ' ';
    }
    cout << endl;

    for (int n:arr){
        cout << n << ' ';
        /** changing the value of n doesn't affect values in the array. */
        n++;
    }
    cout << endl;

    /** but using the reference valuable can change the values in the array! */
}