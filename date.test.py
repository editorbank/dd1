from dd1 import detect

assert('DATE_DDMMYYYY' in detect('31123344'))
assert('DATE_LIKE' in detect('31123344'))
assert('DATE_DDMMYYYY' not in detect('32129999'))
assert('DATE_LIKE' not in detect('32129999'))
assert('DATE_DD_MM_YYYY' not in detect('32.12.9999'))
assert('DATE_DD_MM_YYYY' not in detect('00.00.0000'))
assert('DATE_DD_MM_YYYY' in detect('31.12.9999'))
assert('DATE_DD_MM_YYYY' in detect('01.01.0000'))

assert('DATETIME_LIKE' in detect('31.12.9999 00.00.00'))
assert('DATETIME_LIKE' in detect('9999-12-31T23:59:59'))
assert('DATETIME_LIKE' in detect('99 11 11 23 59'))
assert('DATETIME_LIKE' not in detect('99 11 11 23 60'))

