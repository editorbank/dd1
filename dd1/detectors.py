from re import compile
from .const import *
from .result import result
from json import JSONEncoder,JSONDecoder

class detector():
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

  def to_serializable(self)->dict:
    return {"class":type(self).__name__}

class detector_identified(detector):
  """
  Детектор абстактный с идентификатором
  """
  def __init__(self, id: str = ""):
    super().__init__()
    self.id:str = id if type(id) == str and id != "" else ""

  def ids(self) -> tuple:
    return (self.id,)

  def to_serializable(self)->dict:
    return {**super().to_serializable(),"id":self.id}

class detector_count(detector_identified):
  """
  Детектор количества переданных значений
  """
  def __init__(self, id: str = KEY_LEN):
    super().__init__(id)

  def value(self, value: any):
    self._result.add({self.id:1})

class detector_regexp(detector_identified):
  """
  Детектор на основе регулярного выражения
  """
  def __init__(self, id: str = ..., re: str = ...):
    super().__init__(id)
    self.re = re
    self._re = compile(self.re)

  def value(self, value: any):
    if self._re.match(f"{value}"):
      self._result.add({self.id:1})

  def to_serializable(self)->dict:
    return {**super().to_serializable(),"re":(self.re)}

class detector_type(detector):
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
    return result(**{self.id:len(self._unique)})

  def reset(self):
    self._unique = set()
    return super().reset()


class detector_group(detector):
  """
  Детектор списка значений по группе детекторов
  """
  def __init__(self, detectors:tuple = tuple()):
    super().__init__()
    self.detectors = detectors

  def value(self, value: any):
    for dt in self.detectors:
      dt.value(value)

  def result(self)->result:
    res = result()
    for dt in self.detectors:
      res.add(dt.result())
    return res

  def reset(self):
    for dt in self.detectors:
      dt.reset()
    return super().reset()

  def ids(self) -> tuple:
    ret = []
    for i in self.detectors:
      ret.extend(i.ids())
    return tuple(ret)

  def to_serializable(self)->dict:
    return {**super().to_serializable(),"detectors":[i.to_serializable() for i in self.detectors]}

_all_serializable_detectors = {i.__name__:i for i in (
  detector_count,
  detector_regexp,
  detector_type,
  detector_unique,
  detector_group
)}


class json_dump(JSONEncoder):
  def default(self, o: detector) -> any:
    return o.to_serializable() if issubclass(type(o),detector) else super().default(o)

class json_load(JSONDecoder):
  def __init__(self, *args, **kwargs):
    super().__init__(object_hook = self.object_hook, *args, **kwargs)

  def object_hook(self, dct:dict):
    if CLASS_KEY in dct:
      _class_name = dct[CLASS_KEY]
      dct.pop(CLASS_KEY)
      if _class_name in _all_serializable_detectors:
        return (_all_serializable_detectors[_class_name])(**dct)
    return dct

