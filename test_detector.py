from types import MethodType
from dd1 import value_detector, regexp_detector,  EMPTY_DETECTION
from dd1 import type_detector
import unittest

class TestCase(unittest.TestCase):
  def test_1(self):
    id = "THE_DETECTOR_ID"
    dt = value_detector(id)
    self.assertNotEqual(value_detector().id, id)
    self.assertEqual(dt.id, id)
    self.assertEqual(type(dt.result), MethodType)
    self.assertEqual(type(dt.value), MethodType)
    self.assertEqual(dt.value(None).result(), EMPTY_DETECTION)
    self.assertEqual(dt.value(1111).result(), value_detector(id).value(2222).result())

  def test_2(self):
    id = "HELLO"
    dt = regexp_detector(id, r"^hello$")
    xx = regexp_detector("", r"^hello$")
    self.assertEqual(dt.id, id)
    self.assertNotEqual(xx.id, id)
    self.assertNotEqual(xx.id, "")
    self.assertNotEqual(xx.id, regexp_detector("", r"^hello$").id)
    self.assertEqual(type(xx.id), str)
    self.assertEqual(type(dt.value), MethodType)
    true_result = dt.value("hello").result()
    false_result = dt.value("bye").result()
    self.assertNotEqual(true_result, false_result)

  def test_3(self):
    dt = type_detector()
    self.assertNotEqual(dt.id, None)
    self.assertEqual(dt.value("hello").result(), {"str":1})
    self.assertEqual(dt.value(1111).result(), {"int":1})


if __name__ == "__main__":
  unittest.main()