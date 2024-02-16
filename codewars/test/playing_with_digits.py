from ..src.playing_with_digits import dig_pow
import codewars_test as test


@test.describe("Fixed tests")
def fixed_test():
    @test.it("Samples")
    def sample_tests():
        test.assert_equals(dig_pow(89, 1), 1)
        test.assert_equals(dig_pow(92, 1), -1)
        test.assert_equals(dig_pow(46288, 3), 51)
        test.assert_equals(dig_pow(41, 5), 25)
        test.assert_equals(dig_pow(114, 3), 9)
        test.assert_equals(dig_pow(8, 3), 64)
