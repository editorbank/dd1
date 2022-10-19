@for %%I in (
  tests
  tuner
) do @if exist %%I\dd1 rd /S /Q %%I\dd1
