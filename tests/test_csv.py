from _testlib import *
import json
import unittest

def to_jsonfile(obj,filename=".json"):
  with open(filename,"w", encoding="utf-8") as f:
    json.dump(obj, f, indent=1, ensure_ascii=False)

def from_jsonfile(filename=".json"):
  with open(filename,"r", encoding="utf-8") as f:
    return json.load(f)

def as_jsono(obj)->str:
  return json.dumps(obj, indent=1, ensure_ascii=False)

def as_jsons(s:str)->str:
  return json.dumps(json.loads(s), indent=1, ensure_ascii=False)

received = detect_csv(filename=testdata("0.csv"), delimiter=",", encoding='utf-8')
expected = from_jsonfile(testdata("0.json"))


#print(as_jsono(d))
class TestCase(unittest.TestCase):
  def test_1(self):

    assert(received == expected)
    self.assertEqual(received,expected)

if __name__ == '__main__':
  unittest.main()
