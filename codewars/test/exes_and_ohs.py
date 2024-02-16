import codewars_test as test
from ..src.exes_and_ohs import xo


@test.describe("Sample tests")
def _():
    test_cases = [
        ("ooxx",    True),
        ("xooxx",   False),
        ("ooxXm",   True),
        ("zpzpzpp", True),
        ("zzoo",    False),
        ("oxOx",    True),
        ("",        True),
        ("xxxooo",  True),
        ("xxOo",    True),
        ("o",       False),
    ]
    for s, expected in test_cases:
        @test.it(f"{s=}")
        def _():
            test.assert_equals(xo(s), expected)
