#include "NumXX.hpp"

int main() {
    auto arr1 = numxx::linspace(0.0f, 1.0f, 11, true);
    auto arr2 = numxx::linspace(0.0f, 1.0f, 11, false);

    std::cout << arr1 << std::endl;
    // >> [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ]

    std::cout << arr2 << std::endl;
    // >> [0.        0.0909091 0.1818182 0.2727273 0.3636364 0.4545455 0.5454546 0.6363636 0.7272727 0.8181819 0.9090909]
}
