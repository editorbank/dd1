from sys import argv
from dd1 import loadf
from dd1 import detector
from . import detect_list, detect_csv, escaped_options, read_lines_from_file
import json


def dumps(obj)->str:
  return json.dumps(obj, indent=1, ensure_ascii=False)

def parse_argv(argv)->dict:
  args = {}
  for v in argv:
    vs = v.split("=",maxsplit=2)
    args[vs[0]]=vs[1].encode().decode('unicode-escape') if vs[0] in (escaped_options) else vs[1]
  return args

def help():
    print("""Data Detector v.1 common library
    Use: python -m ddmeter
     or: python -m ddtuner
    """)  

if __name__ == "__main__":
    help()
