from .dd1_num_bin import _SIGN

_DIGIT = "[0-7]"
_C_OCT_PREFIX = r"\\0"

DD1_NUM_OCT = f"^{_DIGIT}+$"
DD1_NUM_OCT_SIG = f"^{_SIGN}?{_DIGIT}+$"
DD1_NUM_OCT_C = f"^{_C_OCT_PREFIX}{_DIGIT}{{3}}$"
