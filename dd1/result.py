import collections

class result(collections.OrderedDict):
  def __init__(self, **kvargs):
    self.update(kvargs)

  def add(self, other: any):
    for i in other:
      self[i] = self[i] + other[i] if i in self else other[i]
