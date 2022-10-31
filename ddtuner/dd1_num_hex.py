from .dd1_num_bin import _SIGN

_DIGIT = "[0-9a-fA-F]"
_C_HEX_PREFIX = r"\\0x"

DD1_NUM_HEX = f"^{_DIGIT}+$"
DD1_NUM_HEX_SIG = f"^{_SIGN}?{_DIGIT}+$"
DD1_NUM_HEX_C = f"^{_C_HEX_PREFIX}{_DIGIT}{_DIGIT}$"
