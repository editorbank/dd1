from dd1 import detect

assert('DATE_DDMMYYYY' in detect('31123344'))
assert('DATE_LIKE' in detect('31123344'))
assert('DATE_DDMMYYYY' not in detect('32129999'))
assert('DATE_LIKE' not in detect('32129999'))
assert('DATE_DD_MM_YYYY' not in detect('32.12.9999'))
assert('DATE_DD_MM_YYYY' not in detect('00.00.0000'))
assert('DATE_DD_MM_YYYY' in detect('31.12.9999'))
assert('DATE_DD_MM_YYYY' in detect('01.01.0000'))
assert('DATE_MM_DD_YYYY' in detect('01.01.0000'))
