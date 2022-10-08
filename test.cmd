python -m unittest||(echo Error in unittest! & exit 1)
@if exist "test/0.csv" >0.tmp python -m dd1 csv filename="test/0.csv" delimiter=","  encoding="utf-8"
@if exist "test/1.csv" >1.tmp python -m dd1 csv filename="test/1.csv" encoding="utf-8"
@if exist "test/2.csv" >2.tmp python -m dd1 csv filename="test/2.csv" encoding="utf-8" quotechar="\x22"
@if exist "test/3.csv" >3.tmp python -m dd1 csv filename="test/3.csv" encoding="windows-1251"
@if exist "test/4.csv" >4.tmp python -m dd1 csv filename="test/4.csv" encoding="windows-1251"
@if exist "test/5.csv" >5.tmp python -m dd1 csv filename="test/5.csv" delimiter="\t" encoding="utf-8"
@if exist "test/6.csv" >6.tmp python -m dd1 csv filename="test/6.csv" delimiter="\t" encoding="utf-8"
@if exist "test/7.csv" >7.tmp python -m dd1 csv filename="test/7.csv" delimiter=","  encoding="utf-8"
@if exist "test/8.csv" >8.tmp python -m dd1 csv filename="test/8.csv"
@if exist "test/9.csv" >9.tmp python -m dd1 csv filename="test/9.csv" delimiter=";"
@for %%I in ( test\*.json ) do @if exist %%~nI.tmp fc %%~nI.tmp %%I >Error.tmp||(echo Error! See Error.tmp & exit 1)
@if exist *.tmp del *.tmp
@echo OK 
