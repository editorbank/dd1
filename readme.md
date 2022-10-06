# Data Detector v1
Утилита для анализа данных.

## Принцип действия
На данном этапе анализу подвергаются только строковые данные.
Строовое значение подвергается проверкам набором регулярных выражений.
Закаждым регулярным выражением закрепляется уникальный тэг (сторока латинских символов в верхнем, цифр и знака `_`).
Если проверяемое значение удовлетворяет регулярному выражению, его тэг добавляется в результирующий набор.

## Примеры запуска

Любые ОС:
```
python -m dd1
python -m dd1 tags
python -m dd1 value 0
python -m dd1 list 0 1 -2 aaa
```

linux:
```
python -m dd1 csv filename=test/data-20200115T1130-structure-20200115T1130.csv encoding=utf-8 'quotechar="' >out.json
```

windows:
```
python -m dd1 csv filename=test/data-20200115T1130-structure-20200115T1130.csv encoding=utf-8 quotechar=\^"
python -m dd1 csv filename=test/data-20200115T1130-structure-20200115T1130.csv encoding=utf-8 quotechar=\^" >out.json
```