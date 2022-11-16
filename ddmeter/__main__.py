import argparse
from dd1 import loadf, dumps
from dd1 import detector
from dd1 import detect_list, detect_csv, escaped_options, read_lines_from_file, file_options, filter_key_for, reader_options

def get_args_parser():
  default_charset = "utf-8"
  default_dds_json = "default.dds"

  main_parser = argparse.ArgumentParser(prog="python -m ddmeter",add_help=False)
  main_parser.add_argument("-h","--help", action="help",help="show this message and exit") 
  # main_parser.add_argument("-v", "--version", action='version', version="%(prog)s "+__version__)
  dds1 = main_parser.add_argument_group("Data detector source from json file (default)")
  dds1.add_argument("-j", "--dds-json-file", help=f"JSON file name (default: \"%(default)s\")", default=default_dds_json)
  dds1.add_argument("-jc", "--dds-json-charset", help=f"JSON file Charset (default: \"%(default)s\")", default=default_charset)
  # dds2 = main_parser.add_argument_group("data detector source from SQLite DB")
  # dds2.add_argument("-b", "--dds-db-file",  help="data detectors sqlite db file")
  # dds2.add_argument("-u", "--dds-db-user",  help="data detectors sqlite db user")
  # dds2.add_argument("-p", "--dds-db-password", help="data detectors sqlite db password")

  file_parser = argparse.ArgumentParser(add_help=False)
  file_parser.add_argument("filename", help="file name") 
  file_parser.add_argument("-c", "--encoding", help=f"charset (default: \"%(default)s\")", default=default_charset)
  file_parser.add_argument("-n", "--newline", help=f"newline character (default: \"%(default)s\")", default="\\n")

  commad_subparsers = main_parser.add_subparsers(dest="subcommad", title="Subcommands", help="Subcommand help: \"%(prog)s subcommand -h\"")

  values_parser = commad_subparsers.add_parser("values")
  values_parser.add_argument( dest='values',nargs='+')

  lines_parser = commad_subparsers.add_parser("lines", parents=[file_parser])

  csv_parser = commad_subparsers.add_parser("csv", parents=[file_parser])
  csv_parser.add_argument("-d", "--delimiter", help="delimiter of values (default: \"%(default)s\")", default=";") 
  for option in reader_options:
    if option not in ("delimiter",):
      csv_parser.add_argument(f"--{option}")

  return main_parser

def args_unescape(args:dict)->dict:
  return {k:v.encode().decode('unicode-escape') if k in (escaped_options) else v for k,v in args.items() if v}

if __name__ == "__main__":
  args_parser = get_args_parser()
  args = args_unescape(args_parser.parse_args().__dict__)
  dds:detector = loadf(args["dds_json_file"])
  func = args["subcommad"]

  if func == "tags":
    print(dumps(sorted(dds.ids())))
  elif func == "values":
    print(dumps(detect_list(dds, args["values"])))
  elif func == "lines":
    print(dumps(detect_list(dds, read_lines_from_file(**filter_key_for(("filename",)+file_options,args)))))
  elif func == "csv":
    print(dumps(detect_csv(dds, **filter_key_for(("filename",)+escaped_options,args))))
  else:
    args_parser.print_help()
