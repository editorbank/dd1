from dd1 import *
import unittest

class TestCase(unittest.TestCase):
  def test_1(self):

    assert('EMAIL_GOOD' in detect_value('a@b'))
    assert('EMAIL_LIKE' in detect_value('a@b'))  
    assert('EMAIL_RFC822' in detect_value('a@b'))
    assert(KEY_STRING in detect_value('a@b'))

    assert('EMAIL_LIKE' in detect_value("!#$%&'*+-/=?^_`{}|~09azAZ@aa.bb"))
    assert('EMAIL_RFC822' in detect_value("!#$%&'*+-/=?^_`{}|~09azAZ@aa.bb"))
    assert(KEY_STRING in detect_value("!#$%&'*+-/=?^_`{}|~09azAZ@aa.bb"))

    assert('EMAIL_RFC822' in detect_value('"aaa bbb"@xxx.yy'))
    assert(KEY_STRING in detect_value('"aaa bbb"@xxx.yy'))

    assert('EMAIL_GOOD' in detect_value("1e.z'_1a-Z-@a.b"))
    assert('EMAIL_LIKE' in detect_value("1e.z'_1a-Z-@a.b"))
    assert('EMAIL_RFC822' in detect_value("1e.z'_1a-Z-@a.b"))
    assert(KEY_STRING in detect_value("1e.z'_1a-Z-@a.b"))

    assert('EMAIL_RFC822' in detect_list(['a@b', "!#$%&'*+-/=?^_`{}|~09azAZ@aa.bb", '"aaa bbb"@xxx.yy', "1e.z'_1a-Z-@a.b"]))
    assert(KEY_STRING in detect_list(['a@b', "!#$%&'*+-/=?^_`{}|~09azAZ@aa.bb", '"aaa bbb"@xxx.yy', "1e.z'_1a-Z-@a.b"]))

if __name__ == '__main__':
  unittest.main()
