#include "NumXX.hpp"

int main() {
    auto original = numxx::zeros<float>({2, 2});
    auto like = numxx::full_like(original, 7.0);

    std::cout << like << std::endl;
    // >> [[7 7]
    //     [7 7]]
}
