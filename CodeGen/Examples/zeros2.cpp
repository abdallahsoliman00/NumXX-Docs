#include "NumXX.hpp"

// Custom Type
struct MyType
{
    std::string str;

    MyType() : str("default") {}
    MyType(std::string s) : str(s) {}

    // Needs a << print overload for NArray to print it
    friend std::ostream &operator<<(std::ostream &os, const MyType &obj)
    {
        os << obj.str;
        return os;
    }
};

int main()
{
    // Calls the default constructor of MyType
    auto a = numxx::zeros<MyType>(3);
    std::cout << a;
    // >> [default default default]
}