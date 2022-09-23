from .dd1_num_bin import _SIGN

_DIGIT = "[0-9]"

DD1_NUM = f"^{_DIGIT}+$"
DD1_NUM_SIG = f"^{_SIGN}?{_DIGIT}+$"
