#include "NumXX.hpp"

int main() {
    auto mat = numxx::ones<float>({2, 3});
    auto arr = numxx::ones<float>(5);

    std::cout << mat << std::endl;
    // >> [[1 1 1]
    //     [1 1 1]]
    std::cout << arr << std::endl;
    // >> [1 1 1 1 1]
}
