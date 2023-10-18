/** input and output set like a module*/
#include <iostream>

/** you can remove the 'std' namespace tag.
 * Simply remove only the std:: in the command below.
*/
using namespace std;

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

    /** the double shift splits each of the chunks */
    std::cout << "Hello, world" << 10 << 'c' << std::endl;

    ::cout << "Hello, world" << endl;
    /** the word 'endl' means 'end line' 
     * it can be replaced '\n'.
    */
}
