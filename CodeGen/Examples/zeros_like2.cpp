#include "NumXX.hpp"

// Custom Type
struct MyType {
    std::string str;

    MyType() : str("default") {}
    MyType(std::string s) : str(s) {}

    // Needs a << print overload for NArray to print it
    friend std::ostream &operator<<(std::ostream &os, const MyType &obj) {
        os << obj.str;
        return os;
    }
};

int main() {
    // Calls the default constructor of MyType
    auto ref_arr = std::vector({1,1,2});
    auto new_arr = numxx::zeros_like<MyType>(ref_arr);

    auto ref_matrix = numxx::NArray({{1,1,2}, {3,4,0}});
    auto new_matrix = numxx::zeros_like<MyType>(ref_matrix);

    std::cout << new_arr;
    // >> [default default default]

    std::cout << new_matrix;
    // >> [[default default default]
    //     [default default default]]
}

