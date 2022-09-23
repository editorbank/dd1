import dd1

d = dd1.detect("0123456789")
assert("NUM" in d)
assert("NUM_SIG" in d)
assert("NUM_HEX" in d)
assert("NUM_HEX_SIG" in d)

d = dd1.detect("0123456789abCDef")
assert("NUM_HEX" in d)
assert("NUM_HEX_SIG" in d)

d = dd1.detect("-0123456789abCDef")
assert("NUM_HEX" not in d)
assert("NUM_HEX_SIG" in d)

d = dd1.detect("+0123456789abCDef")
assert("NUM_HEX" not in d)
assert("NUM_HEX_SIG" in d)

d = dd1.detect("hello")
assert("NUM" not in d)
assert("NUM_SIG" not in d)
assert("NUM_HEX" not in d)
assert("NUM_HEX_SIG" not in d)

d = dd1.detect("\\0x00")
assert("NUM" not in d)
assert("NUM_SIG" not in d)
assert("NUM_HEX" not in d)
assert("NUM_HEX_SIG" not in d)
assert("C_HEX_WORD" not in d)
assert("C_HEX_BYTE" in d)

d = dd1.detect("\\0xff")
assert("NUM" not in d)
assert("NUM_SIG" not in d)
assert("NUM_HEX" not in d)
assert("NUM_HEX_SIG" not in d)
assert("C_HEX_WORD" not in d)
assert("C_HEX_BYTE" in d)

print("OK")