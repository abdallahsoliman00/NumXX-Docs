#include "NumXX.hpp"

int main() {
    auto I = numxx::identity<float>(4);

    std::cout << I << std::endl;
    // >> [[1 0 0 0]
    //     [0 1 0 0]
    //     [0 0 1 0]
    //     [0 0 0 1]]
}
