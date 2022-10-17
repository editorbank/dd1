@(echo tags...)  &python -B -m dd1 tags                                      >tests\data\tags.json
@(echo values...)&python -m dd1 values 0 1 -2 aaa 1                          >tests\data\values.json
@(echo lines...) &python -B -m dd1 lines filename=readme.md encoding="utf-8" >tests\data\lines.json

@if exist tests\data\0.csv (echo 0...)&python -B -m dd1 csv filename="tests\data\0.csv" delimiter=","  encoding="utf-8"   >tests\data\0.json
@if exist tests\data\1.csv (echo 1...)&python -B -m dd1 csv filename="tests\data\1.csv" encoding="utf-8"                  >tests\data\1.json
@if exist tests\data\2.csv (echo 2...)&python -B -m dd1 csv filename="tests\data\2.csv" encoding="utf-8" quotechar="\x22" >tests\data\2.json
@if exist tests\data\3.csv (echo 3...)&python -B -m dd1 csv filename="tests\data\3.csv" encoding="windows-1251"           >tests\data\3.json
@if exist tests\data\4.csv (echo 4...)&python -B -m dd1 csv filename="tests\data\4.csv" encoding="windows-1251"           >tests\data\4.json
@if exist tests\data\5.csv (echo 5...)&python -B -m dd1 csv filename="tests\data\5.csv" delimiter="\t" encoding="utf-8"   >tests\data\5.json
@if exist tests\data\6.csv (echo 6...)&python -B -m dd1 csv filename="tests\data\6.csv" delimiter="\t" encoding="utf-8"   >tests\data\6.json
@if exist tests\data\7.csv (echo 7...)&python -B -m dd1 csv filename="tests\data\7.csv" delimiter=","  encoding="utf-8"   >tests\data\7.json
@if exist tests\data\8.csv (echo 8...)&python -B -m dd1 csv filename="tests\data\8.csv"                                   >tests\data\8.json
@if exist tests\data\9.csv (echo 9...)&python -B -m dd1 csv filename="tests\data\9.csv" delimiter=";"                     >tests\data\9.json
@echo OK