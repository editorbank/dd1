import unittest
from types import MethodType
from dd1 import detector_count, detector_regexp,  RESULT_EMPTY
from dd1 import detector_pytype
from dd1 import KEY_LEN
from dd1 import detector, detector_group, detector_identified
from dd1 import result

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
    self.assertNotEqual(detector_identified().id, id)
    self.assertEqual(dt.id, id)
    dt.reset(); self.assertEqual(dt.id, id)
    self.assertEqual(dt.result(), RESULT_EMPTY)
    self.assertEqual(dt.result(), detector_count().result())

  def test_detector_count(self):
    id = "OTHER_NAME"
    dt = detector_count()
    self.assertEqual(detector_count().id, KEY_LEN)
    self.assertNotEqual(dt.id, id)
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
    dt.value("hello"); self.assertEqual(dt.result(), {"str":1})
    dt.reset(); dt.value(1111); self.assertEqual(dt.result(), {"int":1})
    dt.value(2222); self.assertEqual(dt.result(), {"int":2})
    dt.reset(); self.assertEqual(dt.result(), RESULT_EMPTY)

  def test_4(self):
    dt = detector_group(detectors = [
      detector_pytype(),
      detector_regexp("HELLO", r"^hello$")
    ])
    self.assertEqual(dt.result(), RESULT_EMPTY)
    dt.value("hello"); self.assertEqual(dt.result(), {"str":1, "HELLO":1})
    dt.reset(); dt.value(1111); self.assertEqual(dt.result(), {"int":1})
    dt.reset(); dt.value(1111); dt.value("hello"); self.assertEqual(dt.result(), {"int":1,"str":1, "HELLO":1})

if __name__ == "__main__":
  unittest.main()
