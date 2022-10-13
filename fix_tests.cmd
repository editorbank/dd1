@(echo tags...)  &python -B -m dd1 tags                                      >test\tags.json
@(echo values...)&python -m dd1 values 0 1 -2 aaa 1                          >test\values.json
@(echo lines...) &python -B -m dd1 lines filename=readme.md encoding="utf-8" >test\lines.json

@if exist "test/0.csv" (echo 0...)&python -B -m dd1 csv filename="test/0.csv" delimiter=","  encoding="utf-8"   >test\0.json
@if exist "test/1.csv" (echo 1...)&python -B -m dd1 csv filename="test/1.csv" encoding="utf-8"                  >test\1.json
@if exist "test/2.csv" (echo 2...)&python -B -m dd1 csv filename="test/2.csv" encoding="utf-8" quotechar="\x22" >test\2.json
@if exist "test/3.csv" (echo 3...)&python -B -m dd1 csv filename="test/3.csv" encoding="windows-1251"           >test\3.json
@if exist "test/4.csv" (echo 4...)&python -B -m dd1 csv filename="test/4.csv" encoding="windows-1251"           >test\4.json
@if exist "test/5.csv" (echo 5...)&python -B -m dd1 csv filename="test/5.csv" delimiter="\t" encoding="utf-8"   >test\5.json
@if exist "test/6.csv" (echo 6...)&python -B -m dd1 csv filename="test/6.csv" delimiter="\t" encoding="utf-8"   >test\6.json
@if exist "test/7.csv" (echo 7...)&python -B -m dd1 csv filename="test/7.csv" delimiter=","  encoding="utf-8"   >test\7.json
@if exist "test/8.csv" (echo 8...)&python -B -m dd1 csv filename="test/8.csv"                                   >test\8.json
@if exist "test/9.csv" (echo 9...)&python -B -m dd1 csv filename="test/9.csv" delimiter=";"                     >test\9.json
@echo OK