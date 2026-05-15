#include "NumXX.hpp"

int main() {
    auto arr = numxx::zeros<double>(5);
    auto shallow = numxx::copy(arr);
    // `shallow` shares data with `arr`, so they both share the same memory.

    std::cout << arr.get_start_address() << std::endl;
    // >> 0xa000003e0

    std::cout << shallow.get_start_address() << std::endl;
    // >> 0xa000003e0
}
