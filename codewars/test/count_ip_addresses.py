import unittest
from ..src.count_ip_addresses import ips_between


class TestIpsBetween(unittest.TestCase):

    def test_ips_between_same_network(self):
        start = "10.0.0.0"
        end = "10.0.0.50"
        expected = 50
        actual = ips_between(start, end)
        self.assertEqual(actual, expected)

    def test_ips_between_different_network(self):
        start = "10.0.0.0"
        end = "10.0.1.0"
        expected = 256
        actual = ips_between(start, end)
        self.assertEqual(actual, expected)

    def test_ips_between_different_network_nonzero_start(self):
        start = "20.0.0.10"
        end = "20.0.1.0"
        expected = 246
        actual = ips_between(start, end)
        self.assertEqual(actual, expected)

    def test_ips_between_big_gap(self):
        start = "10.0.0.0"
        end = "20.0.0.0"
        expected = 167772160
        actual = ips_between(start, end)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
