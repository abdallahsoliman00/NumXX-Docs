#include "NumXX.hpp"

int main() {
    auto arr = numxx::NArray({14, 3, 2, 56});
    auto new_arr = numxx::zeros_like(arr);

    auto vec = std::vector({10.0, 23.2, 1.3});
    auto other_arr = numxx::zeros_like(vec);

    std::cout << new_arr;
    // >> [0 0 0 0]

    std::cout << other_arr;
    // >> [0 0 0]
}
