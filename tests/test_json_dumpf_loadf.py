from json import dumps, loads
import unittest
from dd1 import *

class TestCase(unittest.TestCase):

  def test_dumpf_loadf(self):
    o1 = detector_group(
      detectors=[
        detector_count(),
        detector_regexp(id="HELLO",re=r"(?i)^hello$"),
        detector_type(),
        detector_group([
          detector_group([
            detector_unique()
          ])
        ])
      ]
    )
    test_filename = "test1.dds.tmp"
    if os.path.isfile(test_filename):
      os.remove(test_filename)
    dumpf(o1, filename=test_filename, indent=4)
    o2 = loadf(filename=test_filename)
    assert o1.to_serializable() == o2.to_serializable()

if __name__ == "__main__":
  unittest.main()
