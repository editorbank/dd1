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

assert("NUM" not in detect("\\0x00"))
assert("NUM_SIG" not in detect("\\0x00"))
assert("NUM_HEX" not in detect("\\0x00"))
assert("NUM_HEX_SIG" not in detect("\\0x00"))
assert("NUM_HEX_C" in detect("\\0x00"))

assert("NUM" not in detect("\\0xff"))
assert("NUM_SIG" not in detect("\\0xff"))
assert("NUM_HEX" not in detect("\\0xff"))
assert("NUM_HEX_SIG" not in detect("\\0xff"))
assert("NUM_HEX_C" in detect("\\0xff"))
assert("NUM_HEX_C" not in detect("\\0xf"))
assert("NUM_HEX_C" not in detect("\\0xfff"))
