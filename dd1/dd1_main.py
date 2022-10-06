DD1_EMPTY_ONLY = "^$"

_SPACE = r"\s"
_LATIN = r"A-Za-z"
_CYRILIC = r"А-Яа-я"
_DIGIT = r"0-9"
_SIGNS = r"\-+`~!@#\$%^&*(){}\[\]\\|/;:\'\"<,>./?"

DD1_SPACE_ONLY = f"^[{_SPACE}]+$"
DD1_LATIN_ONLY = f"^[{_LATIN}]+$"
DD1_CYRILIC_ONLY = f"^[{_CYRILIC}]+$"
DD1_DIGIT_ONLY = f"^[{_DIGIT}]+$"
DD1_LATIN_TEXT = f"^[{_LATIN}{_DIGIT}{_SPACE}{_SIGNS}]*$"
DD1_CYRILIC_TEXT = f"^[{_CYRILIC}{_DIGIT}{_SPACE}{_SIGNS}]*$"
# print(f"{DD1_CYRILIC_TEXT}") 