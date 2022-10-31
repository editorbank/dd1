from json import dumps, loads
import unittest
from dd1 import *
# from dd1.main_detector import GLOBAL_DETECTOR

class TestCase(unittest.TestCase):
  def _test_schema(self, o1:detector):
    # print(f"{o1=}")
    s1 = dumps(o1, indent=4)
    # print(f"{s1}")
    o2 = loads(s=s1)
    # print(f"{o2=}")
    s2 = dumps(o2, indent=4)
    # print(f"{s2}")
    assert s1 == s2
    assert o1.to_serializable() == o2.to_serializable()

  def test_1(self):
    self._test_schema(
      detector_group((
        detector_count(),
        detector_regexp(id="HELLO",re=r"(?i)^hello$"),
        detector_type(),
        detector_group((
          detector_group((
            detector_unique(),
          )),
        )),
      ))
    )
  
  # def test_2(self):
  #   self._dumps_loads(GLOBAL_DETECTOR)

if __name__ == "__main__":
  unittest.main()
