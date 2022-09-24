from re import escape
from sys import argv
from .__init__ import detect

if __name__ == "__main__":
    if len(argv)>=1:
        for i in range(1,len(argv)):
            print(f"assert(detect({argv[i]!r})=={detect(argv[i])})")
