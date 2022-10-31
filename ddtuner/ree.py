import os
import re

from dd1.read_lines_from_file import read_lines_from_file



def module_path(filename:str):
  this_module_path = os.path.dirname(__file__)
  return os.path.join(this_module_path,filename)


def res_file(filename:str)->str:
  return "".join(read_lines_from_file(module_path(filename)))

def res_str(res:str)->str:
  return "".join(re.split(r"\n|\r\n|\r",res))

def _clear_comments_and_external_spaces(lines:list):
  return [re.sub(r"^\s*[#].*$|(^\s+|\s+$)","",line) for line in lines]

def ree_file(filename:str)->str:
  return "".join(_clear_comments_and_external_spaces(read_lines_from_file(module_path(filename))))

def ree(ree:str)->str:
  return "".join(_clear_comments_and_external_spaces(re.split(r"\n|\r\n|\r",ree)))