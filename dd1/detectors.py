from re import compile
from .const import *
from .result import result

class detector:
  """
  Детектор абстактный
  """
  def __init__(self):
    """Конструктор"""
    super().__init__()
    self._result = result()

  def value(self, value: any):
    """Метод передачи значения детектору. Может вызываться несколько раз."""
    pass

  def result(self)->result:
    """Получение результата анализа"""
    return self._result

  def reset(self):
    """Сброс детектора в начальное состояние"""
    self._result = result()

  def ids(self)->tuple:
    return tuple()

class detector_identified(detector):
  """
  Детектор с идентификатором
  """
  def __init__(self, id: str = ""):
    super().__init__()
    self._id:str = id if type(id) == str and id != "" else ""

  def ids(self) -> tuple:
    return (self._id,)

class detector_count(detector_identified):
  """
  Детектор количества переданных значений
  """
  def __init__(self, id: str = KEY_LEN):
    super().__init__(id)

  def value(self, value: any):
    self._result.add({self._id:1})

class detector_regexp(detector_identified):
  """
  Детектор на основе регулярного выражения
  """
  def __init__(self, id: str = ..., re: str = ...):
    super().__init__(id)
    self._re = compile(re)

  def value(self, value: any):
    if self._re.match(f"{value}"):
      self._result.add({self._id:1})

class detector_pytype(detector):
  """
  Детектор типа python
  """
  _known_types = (str,bytes,int,float)
  _known_ids = (KEY_STRING, KEY_STRING, KEY_NUMBER, KEY_NUMBER)

  def value(self, value: any):
    _type = type(value)
    _typename = (self._known_ids[self._known_types.index(_type)] if _type in self._known_types else self.TYPE_UNKNOWN)
    self._result.add({_typename:1})

  def ids(self)->tuple:
    return (KEY_INCOMPATIBLE, KEY_STRING, KEY_NUMBER)

class detector_unique(detector_identified):
  """
  Детектор количества уникальных значений в списке
  """
  def __init__(self, id: str = KEY_UNIQUE):
    super().__init__(id)
    self._unique = set()

  def value(self, value: any):
    self._unique.add(value)

  def result(self)->result:
    return result(**{self._id:len(self._unique)})

  def reset(self):
    self._unique = set()
    return super().reset()


class detector_group(detector):
  """
  Детектор списка значений по группе детекторов
  """
  def __init__(self, *detectors: tuple):
    super().__init__()
    self._detectors = set(detectors)

  def value(self, value: any):
    for dt in self._detectors:
      dt.value(value)

  def result(self)->result:
    res = result()
    for dt in self._detectors:
      res.add(dt.result())
    return res

  def reset(self):
    for dt in self._detectors:
      dt.reset()
    return super().reset()

  def ids(self) -> tuple:
    ret = []
    for i in self._detectors:
      ret.extend(i.ids())
    return tuple(ret)