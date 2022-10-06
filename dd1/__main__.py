from sys import argv
from . import detect, detect_list, detect_csv, alltags 
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
        print(dumps(list(sorted(detect(argv[i])))))
    elif func == "list" and len(argv) > 2:
      print(dumps(detect_list(argv[2:])))
    elif func == "csv" and len(argv) > 2:
      args = {}
      for v in argv[2:]:
        vs = v.split("=",maxsplit=2)
        args[vs[0]]=vs[1]
      print(dumps(detect_csv(**args)))
    else:
      print("Undefined function!")  
  else:
    print("""Data Detector v.1
    Use: python -m dd1 <function> [<param1> [<param2> [...]]]
    Functions: tags|value|list|csv
    """)  

  # if len(argv)>=1:
    # for i in range(1,len(argv)):
      # print(f"assert(detect({argv[i]!r})=={detect_str(argv[i])})")
    # print(f"assert(detect_list({argv[1:]!r})=={detect_list(argv[1:])!r})")
    # for v in sorted(detect_list(argv[1:])["all"]):
      # print(f"assert({v!r} in detect_list({argv[1:]!r}))")

