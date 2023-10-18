/** input and output set like a module*/
#include <iostream>

namespace a
{
    int n;
}

namespace b
{
    int n;
}

int main(){
    /**
     * The 'std' namespace is a way to differentiate variables. 
     * if two variables have the same name but different namespaces (Here, the last name functions as the namespace.)
     * they can be compared using the namespace.
     */

    a::n = 10;
    b::n = 20;
    std::cout << "Hello, world" << std::endl;
}