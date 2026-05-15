#include "NumXX.hpp"

int main() {
    auto arr = numxx::zeros<double>(5);
    auto deep = numxx::deepcopy(arr);
    // `deep` now has independent memory to `arr`

    std::cout << arr.get_start_address() << std::endl;
    // >> 0xa000003e0

    std::cout << deep.get_start_address() << std::endl;
    // >> 0xa00000450
}
