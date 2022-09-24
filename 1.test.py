from dd1 import detect

assert("NUM" in detect("0123456789"))
assert("NUM_SIG" in detect("0123456789"))
assert("NUM_HEX" in detect("0123456789"))
assert("NUM_HEX_SIG" in detect("0123456789"))

assert("NUM_HEX" in detect("0123456789abCDef"))
assert("NUM_HEX_SIG" in detect("0123456789abCDef"))

assert("NUM_HEX" not in detect("-0123456789abCDef"))
assert("NUM_HEX_SIG" in detect("-0123456789abCDef"))

assert("NUM_HEX" not in detect("+0123456789abCDef"))
assert("NUM_HEX_SIG" in detect("+0123456789abCDef"))

assert("NUM" not in detect("hello"))
assert("NUM_SIG" not in detect("hello"))
assert("NUM_HEX" not in detect("hello"))
assert("NUM_HEX_SIG" not in detect("hello"))

assert("NUM" not in "\\0x00")
assert("NUM_SIG" not in "\\0x00")
assert("NUM_HEX" not in "\\0x00")
assert("NUM_HEX_SIG" not in "\\0x00")
assert("C_HEX_WORD" not in "\\0x00")
assert("C_HEX_BYTE" in "\\0x00")

assert("NUM" not in detect("\\0xff"))
assert("NUM_SIG" not in detect("\\0xff"))
assert("NUM_HEX" not in detect("\\0xff"))
assert("NUM_HEX_SIG" not in detect("\\0xff"))
assert("C_HEX_WORD" not in detect("\\0xff"))
assert("C_HEX_BYTE" in detect("\\0xff"))
