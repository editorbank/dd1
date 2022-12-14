@if exist install.cmd echo Install ...&call install.cmd

@echo Clean ...
@if exist clean.cmd call clean.cmd
@echo Unit tests ...
@python -B -m unittest discover -s tests||(echo Error in unittest! & exit 1)
@echo Console tests ...
@if exist "tests/data/tags.json"   (echo tags...)  &python -B -m dd1 tags                                      >tags.tmp
@if exist "tests/data/values.json" (echo values...)&python -B -m dd1 values 0 1 -2 aaa 1                       >values.tmp
@if exist "tests/data/lines.json"  (echo lines...) &python -B -m dd1 lines filename=readme.md encoding="utf-8" >lines.tmp

@if exist "tests/data/0.csv" (echo 0...)&python -B -m dd1 csv filename="tests/data/0.csv" delimiter=","  encoding="utf-8"   >0.tmp
@if exist "tests/data/1.csv" (echo 1...)&python -B -m dd1 csv filename="tests/data/1.csv" encoding="utf-8"                  >1.tmp
@if exist "tests/data/2.csv" (echo 2...)&python -B -m dd1 csv filename="tests/data/2.csv" encoding="utf-8" quotechar="\x22" >2.tmp
@if exist "tests/data/3.csv" (echo 3...)&python -B -m dd1 csv filename="tests/data/3.csv" encoding="windows-1251"           >3.tmp
@if exist "tests/data/4.csv" (echo 4...)&python -B -m dd1 csv filename="tests/data/4.csv" encoding="windows-1251"           >4.tmp
@if exist "tests/data/5.csv" (echo 5...)&python -B -m dd1 csv filename="tests/data/5.csv" delimiter="\t" encoding="utf-8"   >5.tmp
@if exist "tests/data/6.csv" (echo 6...)&python -B -m dd1 csv filename="tests/data/6.csv" delimiter="\t" encoding="utf-8"   >6.tmp
@if exist "tests/data/7.csv" (echo 7...)&python -B -m dd1 csv filename="tests/data/7.csv" delimiter=","  encoding="utf-8"   >7.tmp
@if exist "tests/data/8.csv" (echo 8...)&python -B -m dd1 csv filename="tests/data/8.csv"                                   >8.tmp
@if exist "tests/data/9.csv" (echo 9...)&python -B -m dd1 csv filename="tests/data/9.csv" delimiter=";"                     >9.tmp
@for %%I in ( test\*.json ) do @if exist %%~nI.tmp fc %%~nI.tmp %%I >Error.tmp||(echo Error! See Error.tmp & exit 1)
@if exist *.tmp del *.tmp
@echo OK 
