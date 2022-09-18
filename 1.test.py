import dd1

d = dd1.detect("0123456789")
assert(dd1.Diagnoses.INTEGER_UNSIGNED in d)
assert(dd1.Diagnoses.INTEGER_SIGNED in d)
assert(dd1.Diagnoses.INTEGER_UNSIGNED_HEXADECIMAL in d)
assert(dd1.Diagnoses.INTEGER_SIGNED_HEXADECIMAL in d)

d = dd1.detect("0123456789abCDef")
assert(dd1.Diagnoses.INTEGER_UNSIGNED_HEXADECIMAL in d)
assert(dd1.Diagnoses.INTEGER_SIGNED_HEXADECIMAL in d)

d = dd1.detect("-0123456789abCDef")
assert(dd1.Diagnoses.INTEGER_UNSIGNED_HEXADECIMAL not in d)
assert(dd1.Diagnoses.INTEGER_SIGNED_HEXADECIMAL in d)

d = dd1.detect("+0123456789abCDef")
assert(dd1.Diagnoses.INTEGER_UNSIGNED_HEXADECIMAL not in d)
assert(dd1.Diagnoses.INTEGER_SIGNED_HEXADECIMAL in d)

d = dd1.detect("hello")
assert(dd1.Diagnoses.INTEGER_UNSIGNED not in d)
assert(dd1.Diagnoses.INTEGER_SIGNED not in d)
assert(dd1.Diagnoses.INTEGER_UNSIGNED_HEXADECIMAL not in d)
assert(dd1.Diagnoses.INTEGER_SIGNED_HEXADECIMAL not in d)

d = dd1.detect("\\0x00")
assert(dd1.Diagnoses.INTEGER_UNSIGNED not in d)
assert(dd1.Diagnoses.INTEGER_SIGNED not in d)
assert(dd1.Diagnoses.INTEGER_UNSIGNED_HEXADECIMAL not in d)
assert(dd1.Diagnoses.INTEGER_SIGNED_HEXADECIMAL not in d)
assert(dd1.Diagnoses.C_HEX_WORD not in d)
assert(dd1.Diagnoses.C_HEX_BYTE in d)

d = dd1.detect("\\0xff")
assert(dd1.Diagnoses.INTEGER_UNSIGNED not in d)
assert(dd1.Diagnoses.INTEGER_SIGNED not in d)
assert(dd1.Diagnoses.INTEGER_UNSIGNED_HEXADECIMAL not in d)
assert(dd1.Diagnoses.INTEGER_SIGNED_HEXADECIMAL not in d)
assert(dd1.Diagnoses.C_HEX_WORD not in d)
assert(dd1.Diagnoses.C_HEX_BYTE in d)
