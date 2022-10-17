from dd1 import detect_list
import unittest

class TestCase(unittest.TestCase):
  def test_1(self):

    assert(detect_list(["110", "-01", "00", "0", "a"])["HOST"] == 5)
    assert(detect_list(["110", "-01", "00", "0", "a"])["HOST_NAME_RFC1123"] == 5)
    assert(detect_list(["110", "-01", "00", "0", "a"])["NUM_HEX_SIG"] == 5)

if __name__ == "__main__":
  unittest.main()
