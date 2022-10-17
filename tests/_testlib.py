import os
import dd1

def detect_value(value):
  return dd1.detect_list(dd1.GLOBAL_DETECTOR,[value])

def detect_list(values):
  return dd1.detect_list(dd1.GLOBAL_DETECTOR,values)

def detect_csv(*args,**kwargs):
  return dd1.detect_csv(detector = dd1.GLOBAL_DETECTOR,*args,**kwargs)

def testdata(filename):
  return os.path.join(os.path.dirname(__file__),"data",filename)