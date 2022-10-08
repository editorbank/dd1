import uuid 
from re import compile

from dd1.const import KEY_LEN

class empty_detection(dict):
  ...

EMPTY_DETECTION = empty_detection()

class the_detection(empty_detection):
  def __init__(self, key: str = "", value: any = ...):
    if key!="":
      self[key] = value


class value_detector:
  """
  Базовый класс и блок обнаружения не None значения 
  """
  def __init__(self, id: str = ""):
    self.id = id if type(id) == str and id != "" else uuid.uuid4().hex
    self._true_result = the_detection(self.id, 1)
    # self._true_result.update(the_detection(KEY_LEN, 1))
    self._value = None

  def value(self, value: any):
    self._value = value
    return self

  def result(self)->the_detection:
    return self._true_result if self._value else EMPTY_DETECTION

class regexp_detector(value_detector):
  """
  Блок обнаружения на основе регулярного выражения
  """
  def __init__(self, id: str = "", re: str = ...):
    super().__init__(id)
    self._re = compile(re)

  def value(self, value: any):
    return super().value(self._re.match(value))

class type_detector(value_detector):
  """
  Детектор типа python
  """
  def value(self, value: any):
    self._true_result = the_detection(type(value).__name__, 1)
    return super().value(True)

