from dd1 import detect_value

assert("NUM" in detect_value("0123456789"))
assert("NUM_SIG" in detect_value("0123456789"))
assert("NUM_HEX" in detect_value("0123456789"))
assert("NUM_HEX_SIG" in detect_value("0123456789"))

assert("NUM_HEX" in detect_value("0123456789abCDef"))
assert("NUM_HEX_SIG" in detect_value("0123456789abCDef"))

assert("NUM_HEX" not in detect_value("-0123456789abCDef"))
assert("NUM_HEX_SIG" in detect_value("-0123456789abCDef"))

assert("NUM_HEX" not in detect_value("+0123456789abCDef"))
assert("NUM_HEX_SIG" in detect_value("+0123456789abCDef"))

assert("NUM" not in detect_value("hello"))
assert("NUM_SIG" not in detect_value("hello"))
assert("NUM_HEX" not in detect_value("hello"))
assert("NUM_HEX_SIG" not in detect_value("hello"))

assert("NUM" not in detect_value("\\0x00"))
assert("NUM_SIG" not in detect_value("\\0x00"))
assert("NUM_HEX" not in detect_value("\\0x00"))
assert("NUM_HEX_SIG" not in detect_value("\\0x00"))
assert("NUM_HEX_C" in detect_value("\\0x00"))

assert("NUM" not in detect_value("\\0xff"))
assert("NUM_SIG" not in detect_value("\\0xff"))
assert("NUM_HEX" not in detect_value("\\0xff"))
assert("NUM_HEX_SIG" not in detect_value("\\0xff"))
assert("NUM_HEX_C" in detect_value("\\0xff"))
assert("NUM_HEX_C" not in detect_value("\\0xf"))
assert("NUM_HEX_C" not in detect_value("\\0xfff"))
