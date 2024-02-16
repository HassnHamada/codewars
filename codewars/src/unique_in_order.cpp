// https://www.codewars.com/kata/54e6533c92449cc251001667/train/cpp

#include <string>
#include <vector>
#include <algorithm>

template <typename T>
std::vector<T> uniqueInOrder(const std::vector<T> &iterable)
{
    std::vector<T> result = iterable;

    result.erase(std::unique(result.begin(), result.end()), result.end());

    return result;
}

std::vector<char> uniqueInOrder(const std::string &iterable)
{
    std::vector<char> characters(iterable.begin(), iterable.end());

    return uniqueInOrder(characters);
}
