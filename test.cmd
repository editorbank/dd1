python -m unittest||(echo Error in unittest! & exit 1)
>0.tmp python -m dd1 csv filename="test/0.csv" delimiter=","  encoding="utf-8"
>1.tmp python -m dd1 csv filename="test/1.csv" encoding="utf-8"
>2.tmp python -m dd1 csv filename="test/2.csv" encoding="utf-8" quotechar="\x22"
>3.tmp python -m dd1 csv filename="test/3.csv" encoding="windows-1251"
>4.tmp python -m dd1 csv filename="test/4.csv" encoding="windows-1251"
>5.tmp python -m dd1 csv filename="test/5.csv" delimiter="\t" encoding="utf-8"
>6.tmp python -m dd1 csv filename="test/6.csv" delimiter="\t" encoding="utf-8"
>7.tmp python -m dd1 csv filename="test/7.csv" delimiter=","  encoding="utf-8"
>8.tmp python -m dd1 csv filename="test/8.csv"
>9.tmp python -m dd1 csv filename="test/9.csv" delimiter=";"
@for %%I in ( test\*.json ) do @fc %%~nI.tmp %%I >Error.tmp||(echo Error! See Error.tmp & exit 1)
@if exist *.tmp del *.tmp
@echo OK 
