#include "NumXX.hpp"

int main()
{
    auto mat = numxx::zeros<float>({2, 3});
    auto arr = numxx::zeros<float>(5);

    std::cout << mat << std::endl;
    // >> [[0 0 0]
    //     [0 0 0]]
    std::cout << arr << std::endl;
    // >> [0 0 0 0 0]
}