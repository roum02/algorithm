#include <iostream>
#include <string>

using namespace std;

int main(){
    string name;
    
    cout << "이름을 입력하세요: " << endl;
    cin >> name;

    string message = "안녕하세요. " + name + "님";
    cout << message << endl;
}