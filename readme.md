# Data Detector v1
Утилита для анализа данных.

## Принцип действия
Утилита анализирует все поступающие строковые значения на предмет соответствия регулярным выражениям.
Каждое регулярное выражение имеет свой идентификатор.
Результатом анализа является словарь, где ключём является идентификатор регулярного выражения,
а значением количество постурающих значений ему соотвующее.
Поступать значения могут из различных источников.
На данный момент поддерживается (задается в командной строке):
* одно значение
* список
* CSV-файл

## Примеры запуска из командной строки

```
python -m dd1
python -m dd1 tags
python -m dd1 value 0
python -m dd1 list 0 1 -2 aaa
python -m dd1 csv filename=test/0.csv encoding=utf-8 quotechar="\x22" >out.tmp
```

## Примеры использования в качестве библиотеки

```
from dd1 import detect_value, detect_list, detect_csv

print(detect_value("110"))
print(detect_list(["110", "-01", "00", "0", "a"]))
print(detect_csv( filename="test/0.csv", encoding="utf-8", quotechar="\x22"))
```
