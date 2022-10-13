from re import compile
from .const import KEY_LEN, KEY_UNIQUE
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


class detector_identified(detector):
  """
  Детектор с идентификатором
  """
  def __init__(self, id: str = ""):
    super().__init__()
    self.id:str = id if type(id) == str and id != "" else ""

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
    self._re = compile(re)

  def value(self, value: any):
    if self._re.match(f"{value}"):
      self._result.add({self.id:1})

class detector_pytype(detector):
  """
  Детектор типа python
  """
  def value(self, value: any):
    self._result.add({type(value).__name__:1})

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
  def __init__(self, detectors: list = []):
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
