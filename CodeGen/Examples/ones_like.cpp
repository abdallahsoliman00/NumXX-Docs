#include "NumXX.hpp"

int main() {
    auto original = numxx::zeros<float>({3, 4});
    auto like = numxx::ones_like(original);

    std::cout << like << std::endl;
    // >> [[1 1 1 1]
    //     [1 1 1 1]
    //     [1 1 1 1]]
}
