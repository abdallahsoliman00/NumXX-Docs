#include "NumXX.hpp"

int main() {
    auto arr = numxx::empty<int>({2, 3});
    // Uninitialised memory - contents are indeterminate
    std::cout << arr.get_shape() << std::endl;
    // >> [2 3]
}
