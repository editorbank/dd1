# Data Detector v1
Утилита для анализа данных.

## Принцип действия
На данном этапе анализу подвергаются только строковые данные.
Строовое значение подвергается проверкам набором регулярных выражений.
Закаждым регулярным выражением закрепляется уникальный тэг (сторока латинских символов в верхнем, цифр и знака `_`).
Если проверяемое значение удовлетворяет регулярному выражению, его тэг добавляется в результирующий набор.