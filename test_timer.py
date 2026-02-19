import unittest
from main import format_time, get_ascii_time

class TestTimer(unittest.TestCase):
    def test_format_time(self):
        self.assertEqual(format_time(0), "00:00")
        self.assertEqual(format_time(60), "01:00")
        self.assertEqual(format_time(90), "01:30")
        self.assertEqual(format_time(3661), "61:01")

    def test_get_ascii_time(self):
        ascii_out = get_ascii_time("00:00")
        lines = ascii_out.split("\n")
        self.assertEqual(len(lines), 8)
        # Check that it contains characters
        for line in lines:
            self.assertTrue(len(line) > 0)

if __name__ == "__main__":
    unittest.main()
