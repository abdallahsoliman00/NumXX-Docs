#include "NumXX.hpp"

int main() {
    auto I = numxx::eye<double>(3);
    auto rect = numxx::eye<double>(2, 4);

    std::cout << I << std::endl;
    // >> [[1 0 0]
    //     [0 1 0]
    //     [0 0 1]]
    std::cout << rect << std::endl;
    // >> [[1 0 0 0]
    //     [0 1 0 0]]
}
