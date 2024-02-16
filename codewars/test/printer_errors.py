import codewars_test as test
from ..src.printer_errors import printer_error


@test.describe("printer_error")
def basic_tests():
    @test.it('Example Test Cases')
    def example_test_cases():
        s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
        test.assert_equals(printer_error(s), "3/56")
        s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
        test.assert_equals(printer_error(s), "6/60")
        s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
        test.assert_equals(printer_error(s), "11/65")

    @test.it('Additional Test Cases')
    def additional_test_cases():
        s = ""
        test.assert_equals(printer_error(s), "0/0")

        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        test.assert_equals(printer_error(s), "0/40")

        s = "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
        test.assert_equals(printer_error(s), "0/38")

        s = "nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn"
        test.assert_equals(printer_error(s), "38/38")
