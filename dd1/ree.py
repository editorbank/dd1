import os
import re

def read_lines_from_file(filename:str):
  this_module_path = os.path.dirname(__file__)
  filepath = os.path.join(this_module_path,filename)
  if os.path.isfile(filepath):
    with open(filepath,'r') as f:
      return [re.sub(r"(\n|\r\n|\r)$","",line) for line in f.readlines()]
  else:
    return []

def res_file(filename:str)->str:
  return "".join(read_lines_from_file(filename))

def res_str(res:str)->str:
  return "".join(re.split(r"\n|\r\n|\r",res))

def _clear_comments_and_external_spaces(lines:list):
  return [re.sub(r"^\s*[#].*$|(^\s+|\s+$)","",line) for line in lines]

def ree_file(filename:str)->str:
  return "".join(_clear_comments_and_external_spaces(read_lines_from_file(filename)))

def ree(ree:str)->str:
  return "".join(_clear_comments_and_external_spaces(re.split(r"\n|\r\n|\r",ree)))