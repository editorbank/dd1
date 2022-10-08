from sys import argv
from . import detect_value, detect_list, detect_csv, alltags, escaped_options
import json

def dumps(obj)->str:
  return json.dumps(obj, indent=1, ensure_ascii=False)

if __name__ == "__main__":
  if len(argv) > 1:
    func = argv[1]
    if func == "tags":
      print(dumps(list(sorted(alltags()))))
    elif func == "value" and len(argv) > 2:
      for i in range(2,len(argv)):
        print(dumps(detect_value(argv[i])))
    elif func == "list" and len(argv) > 2:
      print(dumps(detect_list(argv[2:])))
    elif func == "csv" and len(argv) > 2:
      args = {}
      for v in argv[2:]:
        vs = v.split("=",maxsplit=2)
        args[vs[0]]=vs[1].encode().decode('unicode-escape') if vs[0] in (escaped_options) else vs[1]
      print(dumps(detect_csv(**args)))
    else:
      print("Undefined function!")  
  else:
    print("""Data Detector v.1
    Use: python -m dd1 <function> [<param1> [<param2> [...]]]
    Functions: tags|value|list|csv
    """)  
