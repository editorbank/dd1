from enum import Enum
import re

class Diagnoses(Enum):
  INTEGER_UNSIGNED = "INTEGER_UNSIGNED"
  INTEGER_SIGNED = "INTEGER_SIGNED"
  INTEGER_UNSIGNED_HEXADECIMAL = "INTEGER_UNSIGNED_HEXADECIMAL"
  INTEGER_SIGNED_HEXADECIMAL = "INTEGER_SIGNED_HEXADECIMAL"
  C_HEX_BYTE = "C_HEX_BYTE"
  C_HEX_WORD = "C_HEX_WORD"

def detect(value:str)->dict:
  diagnosis = {}
  if re.match(r"^[0-9]+$", value):
    diagnosis[Diagnoses.INTEGER_UNSIGNED]=True
  if re.match(r"^[-+]?[0-9]+$", value):
    diagnosis[Diagnoses.INTEGER_SIGNED]=True
  if re.match(r"(?i)^[0-9a-f]+$", value):
    diagnosis[Diagnoses.INTEGER_UNSIGNED_HEXADECIMAL]=True
  if re.match(r"(?i)^[-+]?[0-9a-f]+$", value):
    diagnosis[Diagnoses.INTEGER_SIGNED_HEXADECIMAL]=True
  if re.match(r"^\\0x[0-9a-f]{2}$", value):
    diagnosis[Diagnoses.C_HEX_BYTE]=True
  if re.match(r"^\\0x[0-9a-f]{4}$", value):
    diagnosis[Diagnoses.C_HEX_WORD]=True
  return diagnosis