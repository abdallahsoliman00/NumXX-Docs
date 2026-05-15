#include "NumXX.hpp"

int main() {
    auto arr = numxx::full<int>({2, 3}, 42);
    auto vec = numxx::full<double>(5, 3.14);

    std::cout << arr << std::endl;
    // >> [[42 42 42]
    //     [42 42 42]]
    std::cout << vec << std::endl;
    // >> [3.14 3.14 3.14 3.14 3.14]
}
