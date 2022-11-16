@for %%I in (
  tests
  tuner
) do @if not exist %%I\dd1 mklink /D %%I\dd1 %~dp0dd1
