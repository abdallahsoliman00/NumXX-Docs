#include "NumXX.hpp"

int main() {
    auto up = numxx::geomspace(1.0f, 100.0f, 5);
    auto down = numxx::geomspace(100.0f, 1.0f, 5);

    std::cout << up << std::endl;
    // >> [  1.        3.16228  10.       31.62278 100.     ]

    std::cout << down << std::endl;
    // >> [100.       31.62278   10.       3.16228   1.     ]
}
