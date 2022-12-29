# Data Detector v1
Утилита для анализа данных.

## Принцип действия
Утилита анализирует все поступающие строковые значения на предмет соответствия регулярным выражениям.
Каждое регулярное выражение имеет свой идентификатор.
Результатом анализа является словарь, где ключём является идентификатор регулярного выражения,
а значением количество постурающих значений ему соотвующее.
Поступать значения могут из различных источников.


## Примеры запуска из командной строки
На данный момент для вызова из командной строки поддерживается:
* tags - вывод списка возможных тэгов в формате JSON;
* values - одно или список значений из коммандной строки;
* lines - список значений из текстового файла (одна строка = одно значение);
* csv - анализ значений поколоночно из файла формата CSV.
Для текстового и CSV-файла можно указать кодировку, разделитель и пр.
```
python -m dd1
python -m dd1 tags
python -m dd1 values 0
python -m dd1 values 0 1 -2 aaa 1
python -m dd1 lines filename=test/0.json
python -m dd1 csv filename=test/0.csv encoding=utf-8 quotechar="\x22" >out.tmp
```

## Примеры использования в качестве библиотеки
Используются функции
* detect_value - для отдельных значений любого типа
* detect_list - для списков значений любого типа
* detect_csv - для CSV-файлов

```
from dd1 import detect_value, detect_list, detect_csv

print(detect_value("110"))
print(detect_list(["110", "-01", "00", "0", "a"]))
print(detect_csv( filename="test/0.csv", encoding="utf-8", quotechar="\x22"))
```
## Ссылки
* [https://cran.r-project.org/web/packages/daqapo/vignettes/Introduction-to-DaQAPO.html](https://cran.r-project.org/web/packages/daqapo/vignettes/Introduction-to-DaQAPO.html)
