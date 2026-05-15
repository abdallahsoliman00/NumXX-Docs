#include "NumXX.hpp"

int main() {
    auto original = numxx::zeros<float>({3, 4});
    auto like = numxx::empty_like<int>(original);

    std::cout << like.get_shape() << std::endl;
    // >> (2, 3) 
}
