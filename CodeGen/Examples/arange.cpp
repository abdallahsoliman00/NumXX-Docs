#include "NumXX.hpp"

int main() {
    auto arr1 = numxx::arange(10, 1, -1);
    auto arr2 = numxx::arange(0, 1.45, 0.2);

    std::cout << arr1 << std::endl;
    // >> [10  9  8  7  6  5  4  3  2] 

    std::cout << arr2 << std::endl;
    // >> [0.  0.2 0.4 0.6 0.8 1.  1.2 1.4]
}
