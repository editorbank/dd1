_IP1 = "([0-9]|[0-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"
_NAME_RFC1123 = r"([-0-9a-zA-Z]{1,64})"
_NAME_RFC952 = r"([a-zA-Z]|[a-zA-Z][-0-9a-zA-Z]{0,62}[0-9a-zA-Z])"

_IP4 = f"({_IP1}[.]{_IP1}[.]{_IP1}[.]{_IP1})"
DD1_IP4 = f"^{_IP4}$"

_HOST_NAME_RFC1123 = f"({_NAME_RFC1123}([.]{_NAME_RFC1123})*)"
DD1_HOST_NAME_RFC1123 = f"^{_HOST_NAME_RFC1123}*$"

_HOST_NAME_RFC952 = f"({_NAME_RFC952}([.]{_NAME_RFC952})*)"
DD1_HOST_NAME_RFC952 = f"^{_HOST_NAME_RFC952}$"

DD1_HOST = f"^({_IP4}|{_HOST_NAME_RFC1123}|{_HOST_NAME_RFC952})$"

_EMAIL_LOCAL_NAME = r"[!#$%&'*+\-\/=?^_`\{\}|~0-9a-zA-Z]+"
DD1_EMAIL_RFC = f"^{_EMAIL_LOCAL_NAME}@({_IP4}|{_HOST_NAME_RFC1123})$"
