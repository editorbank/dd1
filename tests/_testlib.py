import os
import dd1
import ddtuner

def detect_value(value):
  return dd1.detect_list(ddtuner.GLOBAL_DETECTOR,[value])

def detect_list(values):
  return dd1.detect_list(ddtuner.GLOBAL_DETECTOR,values)

def detect_csv(*args,**kwargs):
  return dd1.detect_csv(detector = ddtuner.GLOBAL_DETECTOR,*args,**kwargs)

def testdata(filename):
  return os.path.join(os.path.dirname(__file__),"data",filename)