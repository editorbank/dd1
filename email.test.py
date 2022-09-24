from dd1 import detect

assert(detect('a@b')==['EMAIL_GOOD', 'EMAIL_LIKE', 'EMAIL_RFC822'])
assert(detect("!#$%&'*+-/=?^_`{}|~09azAZ@aa.bb")==['EMAIL_LIKE', 'EMAIL_RFC822'])
assert(detect('"aaa bbb"@xxx.yy')==['EMAIL_RFC822'])
assert(detect("1e.z'_1a-Z-@a.b")==['EMAIL_GOOD', 'EMAIL_LIKE', 'EMAIL_RFC822'])
