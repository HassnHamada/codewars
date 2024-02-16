from codewars_test import test_framework as Test
from ..src.replace_with_alphabet_position import alphabet_position

Test.describe("Alphabet Position Replacement")

Test.it("should handle empty strings")
Test.assert_equals(alphabet_position(""),
                   "",
                   "Empty string should return an empty string")

Test.it("should handle simple cases")
Test.assert_equals(alphabet_position("a"),
                   "1",
                   "'a' should return '1'")
Test.assert_equals(alphabet_position("z"),
                   "26",
                   "'z' should return '26'")

Test.it("should ignore non-letter characters")
Test.assert_equals(alphabet_position("1"),
                   "",
                   "Non-letter characters should be ignored")
Test.assert_equals(alphabet_position("-!?"),
                   "",
                   "Non-letter characters should be ignored")

Test.it("should handle normal sentences")
Test.assert_equals(alphabet_position("The sunset sets at twelve o' clock."),
                   "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11",
                   "Should return positions of letters as a string")

Test.it("should handle uppercase letters")
Test.assert_equals(alphabet_position("ABC"),
                   "1 2 3",
                   "Uppercase letters should be treated as lowercase")

Test.it("should handle mixed cases and characters")
Test.assert_equals(alphabet_position("Hello, World!"),
                   "8 5 12 12 15 23 15 18 12 4",
                   "Mixed cases and non-letter characters should be handled correctly")
