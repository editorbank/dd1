from .ree import ree

_YY = r"([0-9]{2})"
_Y4 = r"([0-9]{4})"
_MM = r"(0[1-9]|1[0-2])"
_DD = r"(0[1-9]|[12][0-9]|3[01])"
_S = r"[\.\/\-_ :T]"
_HH = r"([01][0-9]|2[0-3])"
_59 = r"([0-5][0-9])"
DD1_DATE_DDMMYY = f"^{_DD}{_MM}{_YY}$"
DD1_DATE_YYMMDD = f"^{_YY}{_MM}{_DD}$"
DD1_DATE_YYDDMM = f"^{_YY}{_DD}{_MM}$"
DD1_DATE_MMDDYY = f"^{_MM}{_DD}{_YY}$"
DD1_DATE_DDMMYYYY = f"^{_DD}{_MM}{_Y4}$"
DD1_DATE_YYYYMMDD = f"^{_Y4}{_MM}{_DD}$"
DD1_DATE_YYYYDDMM = f"^{_Y4}{_DD}{_MM}$"
DD1_DATE_MMDDYYYY = f"^{_MM}{_DD}{_Y4}$"
DD1_DATE_DD_MM_YYYY = f"^{_DD}{_S}{_MM}{_S}{_Y4}$"
DD1_DATE_YYYY_MM_DD = f"^{_Y4}{_S}{_MM}{_S}{_DD}$"
DD1_DATE_YYYY_DD_MM = f"^{_Y4}{_S}{_DD}{_S}{_MM}$"
DD1_DATE_MM_DD_YYYY = f"^{_MM}{_S}{_DD}{_S}{_Y4}$"

_DATE_LIKE = ree(f"""
  (
    {_DD}{_MM}({_YY}|{_Y4})|
    ({_YY}|{_Y4}){_MM}{_DD}|
    ({_YY}|{_Y4}){_DD}{_MM}|
    {_MM}{_DD}({_YY}|{_Y4})|
    {_DD}{_S}{_MM}{_S}({_YY}|{_Y4})|
    ({_YY}|{_Y4}){_S}{_MM}{_S}{_DD}|
    ({_YY}|{_Y4}){_S}{_DD}{_S}{_MM}|
    {_MM}{_S}{_DD}{_S}({_YY}|{_Y4})
  )
""")
DD1_DATE_LIKE = ree(f"^{_DATE_LIKE}$")
DD1_DATETIME_LIKE = ree(f"^{_DATE_LIKE}{_S}{_HH}{_S}{_59}({_S}{_59})?$")
