from ..src.jaden_casing_strings import to_jaden_case
import codewars_test as test


@test.describe('Sample test')
def basic_tests():
    @test.it('Simple text')
    def _():
        quote = "How can mirrors be real if our eyes aren't real"
        expected = "How Can Mirrors Be Real If Our Eyes Aren't Real"
        test.assert_equals(to_jaden_case(quote), expected)

    @test.it('Empty string')
    def _():
        quote = ""
        test.assert_equals(to_jaden_case(quote), "")

    @test.it('String with numbers and punctuation')
    def _():
        quote = "Hello 123. This is a test!"
        test.assert_equals(to_jaden_case(quote), "Hello 123. This Is A Test!")
