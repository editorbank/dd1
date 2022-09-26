from sys import argv
from .__init__ import detect_list

if __name__ == "__main__":
  if len(argv)>=1:
    # for i in range(1,len(argv)):
      # print(f"assert(detect({argv[i]!r})=={detect_str(argv[i])})")
    # print(f"assert(detect_list({argv[1:]!r})=={detect_list(argv[1:])!r})")
    for v in detect_list(argv[1:]):
      print(f"assert({v!r} in detect_list({argv[1:]!r}))")
