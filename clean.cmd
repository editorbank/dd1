@if exist __pycache__ rd /S /Q __pycache__ || exit /b 1
@if exist dd1\__pycache__ rd /S /Q dd1\__pycache__ || exit /b 1
@if exist *.tmp del /S /Q *.tmp || exit /b 1
@echo OK