from .dd1_num_bin import _SIGN

_DIGIT = "[0-7]"
_C_OCT_PREFIX = r"\\"

DD1_NUM_OCT = f"^{_DIGIT}+$"
DD1_NUM_OCT_SIG = f"^{_SIGN}?{_DIGIT}+$"
DD1_NUM_OCT_C = f"""(?x) # восьмеричное число в синтаксисе языка Си
  ^
  {_C_OCT_PREFIX}
  (
    0{{1,3}}
    |
    0?{_DIGIT}{_DIGIT}?
    |
    [1-3]{_DIGIT}{_DIGIT}
  )
  $
  """
