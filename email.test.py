from dd1 import detect, detect_list

assert('EMAIL_GOOD' in detect('a@b'))
assert('EMAIL_LIKE' in detect('a@b'))  
assert('EMAIL_RFC822' in detect('a@b'))
assert('str' in detect('a@b'))

assert('EMAIL_LIKE' in detect("!#$%&'*+-/=?^_`{}|~09azAZ@aa.bb"))
assert('EMAIL_RFC822' in detect("!#$%&'*+-/=?^_`{}|~09azAZ@aa.bb"))
assert('str' in detect("!#$%&'*+-/=?^_`{}|~09azAZ@aa.bb"))

assert('EMAIL_RFC822' in detect('"aaa bbb"@xxx.yy'))
assert('str' in detect('"aaa bbb"@xxx.yy'))

assert('EMAIL_GOOD' in detect("1e.z'_1a-Z-@a.b"))
assert('EMAIL_LIKE' in detect("1e.z'_1a-Z-@a.b"))
assert('EMAIL_RFC822' in detect("1e.z'_1a-Z-@a.b"))
assert('str' in detect("1e.z'_1a-Z-@a.b"))

assert('EMAIL_RFC822' in detect_list(['a@b', "!#$%&'*+-/=?^_`{}|~09azAZ@aa.bb", '"aaa bbb"@xxx.yy', "1e.z'_1a-Z-@a.b"])['all'])
assert('str' in detect_list(['a@b', "!#$%&'*+-/=?^_`{}|~09azAZ@aa.bb", '"aaa bbb"@xxx.yy', "1e.z'_1a-Z-@a.b"])['all'])
