import os
import re

def read_lines_from_file(filename:str):
  this_module_path = os.path.dirname(__file__)
  filepath = os.path.join(this_module_path,filename)
  if os.path.isfile(filepath):
    with open(filepath,'r') as f:
      return [line.rstrip() for line in f.readlines()]
  else:
    return []

def res_file(filename:str)->str:
  return "".join(read_lines_from_file(filename))

def res(res:str)->str:
  return "".join([line.rstrip() for line in res.split("\n")])

def _clear_comments_and_external_spaces(lines:list):
  return [re.sub(r"^\s*[#].*$|(^\s+|\s+$)","",line) for line in lines]

def ree_file(filename:str)->str:
  return "".join(_clear_comments_and_external_spaces(read_lines_from_file(filename)))

def ree(ree:str)->str:
  return "".join(_clear_comments_and_external_spaces([line.rstrip() for line in ree.split("\n")]))