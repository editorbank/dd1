from _testlib import *
import unittest

class TestCase(unittest.TestCase):
  def test_1(self):

    assert('DATE_DDMMYYYY' in detect_value('31123344'))
    assert('DATE_LIKE' in detect_value('31123344'))
    assert('DATE_DDMMYYYY' not in detect_value('32129999'))
    assert('DATE_LIKE' not in detect_value('32129999'))
    assert('DATE_DD_MM_YYYY' not in detect_value('32.12.9999'))
    assert('DATE_DD_MM_YYYY' not in detect_value('00.00.0000'))
    assert('DATE_DD_MM_YYYY' in detect_value('31.12.9999'))
    assert('DATE_DD_MM_YYYY' in detect_value('01.01.0000'))

    assert('DATETIME_LIKE' in detect_value('31.12.9999 00.00.00'))
    assert('DATETIME_LIKE' in detect_value('9999-12-31T23:59:59'))
    assert('DATETIME_LIKE' in detect_value('99 11 11 23 59'))
    assert('DATETIME_LIKE' not in detect_value('99 11 11 23 60'))

if __name__ == '__main__':
  unittest.main()
