#include "NumXX.hpp"

int main() {
    auto arr = numxx::logspace(0.0f, 2.0f, 5);

    std::cout << arr << std::endl;
    // >> [  1.        3.16228  10.       31.62278 100.     ]
}
