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
    print("""Data Detector v.1
    Use: python -m dd1 <function> [<param1> [<param2> [...]]]
    Functions: tags|arg|line|csv
    """)  

if __name__ == "__main__":
  if len(argv) > 1:
    func = argv[1]
    GLOBAL_DETECTOR:detector = loadf("default.dds")

    if func == "tags":
      print(dumps(sorted(GLOBAL_DETECTOR.ids())))
    elif func == "values" and len(argv) > 2:
        print(dumps(detect_list(GLOBAL_DETECTOR, argv[2:])))
    else:
      kwargs = parse_argv(argv[2:])
      if func == "lines" and len(argv) > 2:
        print(dumps(detect_list(GLOBAL_DETECTOR, read_lines_from_file(**kwargs))))
      elif func == "csv" and len(argv) > 2:
        print(dumps(detect_csv(GLOBAL_DETECTOR, **kwargs)))
      else:
        print(f"Undefined function \"{func}\"!")
        help()
  else:
    help()
