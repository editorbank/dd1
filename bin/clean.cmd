@for %%I in (
  *.tmp
  *.pyc
) do @if exist %%I del /S /Q %%I || exit /b 1

@for %%I in (
  .\__pycache__
  dd1\__pycache__
  tests\__pycache__
  tuner\__pycache__
) do @if exist %%I rd /S /Q %%I || exit /b 1

@echo OK