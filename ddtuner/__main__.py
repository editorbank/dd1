from sys import argv
from dd1 import detector, dumpf, dumpf_options, loadf
from .main_detector import GLOBAL_DETECTOR
import json

def dumps(obj)->str:
  return json.dumps(obj, indent=1, ensure_ascii=False)


def parse_argv(argv, escaped_options)->dict:
  args = {}
  for v in argv:
    vs = v.split("=", maxsplit=2)
    args[vs[0]]=vs[1].encode().decode('unicode-escape') if vs[0] in (escaped_options) else vs[1]
  return args

def help():
    print("""Data Detector Schema GENerator
    Use: python -m ddsgen <function> [<param1> [<param2> [...]]]
    Functions: tags|save
    """)  

if __name__ == "__main__":
  if len(argv) > 1:
    func = argv[1]
    if func == "tags":
      print(dumps(sorted(GLOBAL_DETECTOR.ids())))
    elif func == "save":
      kw = parse_argv(argv[2:], dumpf_options)
      if "filename" not in kw:
        kw.update({"filename":"default.dds"})
      print(dumpf(GLOBAL_DETECTOR,**kw))
    else:
      print(f"Undefined function \"{func}\"!")
      help()
  else:
    help()
