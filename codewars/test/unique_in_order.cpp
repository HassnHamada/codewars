#define CATCH_CONFIG_MAIN
#include "catch2/catch_all.hpp"
#include "../src/unique_in_order.cpp"

TEST_CASE("Unique in order works with strings", "[unique_in_order]") {
    REQUIRE(uniqueInOrder("AAAABBBCCDAABBB") == std::vector<char>{'A', 'B', 'C', 'D', 'A', 'B'});
    REQUIRE(uniqueInOrder("ABBCcAD") == std::vector<char>{'A', 'B', 'C', 'c', 'A', 'D'});
    REQUIRE(uniqueInOrder("") == std::vector<char>{});
}

TEST_CASE("Unique in order works with vector of integers", "[unique_in_order]") {
    REQUIRE(uniqueInOrder(std::vector<int>{1,2,2,3,3}) == std::vector<int>{1,2,3});
    REQUIRE(uniqueInOrder(std::vector<int>{1,1,1,1,1}) == std::vector<int>{1});
    REQUIRE(uniqueInOrder(std::vector<int>{}) == std::vector<int>{});
}

TEST_CASE("Unique in order works with vector of characters", "[unique_in_order]") {
    REQUIRE(uniqueInOrder(std::vector<char>{'a','a','b','b','c','c'}) == std::vector<char>{'a','b','c'});
    REQUIRE(uniqueInOrder(std::vector<char>{'a'}) == std::vector<char>{'a'});
    REQUIRE(uniqueInOrder(std::vector<char>{}) == std::vector<char>{});
}

TEST_CASE("Unique in order works with mixed characters", "[unique_in_order]") {
    REQUIRE(uniqueInOrder(std::vector<char>{'a','A','b','B','c','C'}) == std::vector<char>{'a','A','b','B','c','C'});
    REQUIRE(uniqueInOrder(std::vector<char>{'a','a','A','A','b','B','B'}) == std::vector<char>{'a','A','b','B'});
}
