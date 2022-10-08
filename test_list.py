from dd1 import detect_list

assert('HOST' in detect_list(['110', '-01', '00', '0', 'a'])["all"])
assert('HOST_NAME_RFC1123' in detect_list(['110', '-01', '00', '0', 'a'])["all"])
assert('NUM_HEX_SIG' in detect_list(['110', '-01', '00', '0', 'a'])["all"])