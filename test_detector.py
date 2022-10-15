import unittest
from types import MethodType
from dd1 import *

class TestCase(unittest.TestCase):
  def test_detector(self):
    dt = detector()
    self.assertEqual(type(dt.__init__), MethodType)
    self.assertEqual(type(dt.value), MethodType)
    self.assertEqual(type(dt.result), MethodType)
    self.assertEqual(type(dt.reset), MethodType)
    self.assertEqual(dt.result(), RESULT_EMPTY)

  def test_detector_identified(self):
    id = "DETECTOR_NAME"
    dt = detector_identified(id)
    self.assertNotEqual(detector_identified().ids(), (id,))
    self.assertEqual(dt.ids(), (id,))
    dt.reset(); self.assertEqual(dt.ids(), (id,))
    self.assertEqual(dt.result(), RESULT_EMPTY)
    self.assertEqual(dt.result(), detector_count().result())

  def test_detector_count(self):
    id = "OTHER_NAME"
    dt = detector_count()
    self.assertEqual(detector_count().ids(), (KEY_LEN,))
    self.assertNotEqual(dt.ids(), (id,))
    self.assertEqual(type(dt.result), MethodType)
    self.assertEqual(dt.result(), RESULT_EMPTY)
    dt.value(111); self.assertEqual(dt.result(), result(**{KEY_LEN:1}))

  def test_detector_regexp(self):
    id = "HELLO"
    dt = detector_regexp(id, r"^hello$")
    self.assertEqual(dt.result(), RESULT_EMPTY)
    dt.value("hello"); self.assertEqual(dt.result(), {id:1})
    dt.reset(); dt.value("bye"); self.assertEqual(dt.result(), RESULT_EMPTY)

  def test_detector_pytype(self):
    dt = detector_pytype()
    self.assertEqual(dt.result(), RESULT_EMPTY)
    dt.value("hello"); self.assertEqual(dt.result(), {KEY_STRING:1})
    dt.reset(); dt.value(1111); self.assertEqual(dt.result(), {KEY_NUMBER:1})
    dt.value(2222); self.assertEqual(dt.result(), {KEY_NUMBER:2})
    dt.reset(); self.assertEqual(dt.result(), RESULT_EMPTY)

  def test_4(self):
    dt = detector_group(
      detector_pytype(),
      detector_regexp("HELLO", r"^hello$")
    )
    self.assertEqual(dt.result(), RESULT_EMPTY)
    dt.value("hello"); self.assertEqual(dt.result(), {KEY_STRING:1, "HELLO":1})
    dt.reset(); dt.value(1111); self.assertEqual(dt.result(), {KEY_NUMBER:1})
    dt.reset(); dt.value(1111); dt.value("hello"); self.assertEqual(dt.result(), {KEY_NUMBER:1,KEY_STRING:1, "HELLO":1})

if __name__ == "__main__":
  unittest.main()
