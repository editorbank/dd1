@if exist "test/0.csv" >test\0.json python -B -m dd1 csv filename="test/0.csv" delimiter=","  encoding="utf-8"
@if exist "test/1.csv" >test\1.json python -B -m dd1 csv filename="test/1.csv" encoding="utf-8"
@if exist "test/2.csv" >test\2.json python -B -m dd1 csv filename="test/2.csv" encoding="utf-8" quotechar="\x22"
@if exist "test/3.csv" >test\3.json python -B -m dd1 csv filename="test/3.csv" encoding="windows-1251"
@if exist "test/4.csv" >test\4.json python -B -m dd1 csv filename="test/4.csv" encoding="windows-1251"
@if exist "test/5.csv" >test\5.json python -B -m dd1 csv filename="test/5.csv" delimiter="\t" encoding="utf-8"
@if exist "test/6.csv" >test\6.json python -B -m dd1 csv filename="test/6.csv" delimiter="\t" encoding="utf-8"
@if exist "test/7.csv" >test\7.json python -B -m dd1 csv filename="test/7.csv" delimiter=","  encoding="utf-8"
@if exist "test/8.csv" >test\8.json python -B -m dd1 csv filename="test/8.csv"
@if exist "test/9.csv" >test\9.json python -B -m dd1 csv filename="test/9.csv" delimiter=";"