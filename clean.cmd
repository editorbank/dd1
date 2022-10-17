@for %%I in (
  .
  dd1
  tests
) do if exist %%I\__pycache__ rd /S /Q %%I\__pycache__ || exit /b 1
@if exist *.tmp del /S /Q *.tmp || exit /b 1
@echo OK