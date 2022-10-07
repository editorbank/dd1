from dd1 import detect_csv
import json

def to_jsonfile(obj,filename=".json"):
  with open(filename,"w", encoding="utf-8") as f:
    json.dump(obj, f, indent=1, ensure_ascii=False)

def as_jsono(obj)->str:
  return json.dumps(obj, indent=1, ensure_ascii=False)

def as_jsons(s:str)->str:
  return json.dumps(json.loads(s), indent=1, ensure_ascii=False)


# d = detect_csv(filename="test/structure-20200115T1130.csv", encoding='utf-8')
# d = detect_csv(filename="test/data-20200115T1130-structure-20200115T1130.csv", encoding='utf-8', quotechar="\"")
# d = detect_csv(filename="test/structure-20200320T1016.csv", encoding='windows-1251')
# d = detect_csv(filename="test/data-20200320T1016-structure-20200320T1016.csv", encoding='windows-1251')
# d = detect_csv(filename="test/419_doma_rebenka.csv",delimiter="\t", encoding='utf-8')
# d = detect_csv(filename="test/581_raspolozhenie_mest_priyoma_dokumentov_departamenta_zemelnyh_resursov_goroda_moskvy.csv",delimiter="\t", encoding='utf-8')
# d = detect_csv(filename="test/anylised_messages_tag.csv",delimiter=",", encoding='utf-8')
# d = detect_csv(filename="test/phone_data.csv")
# d = detect_csv(filename="test/Missouri_Active_Alcohol_License_Data (Excel (Europe)).csv",delimiter=";")
d = detect_csv(filename="test/data1.csv", delimiter=",", encoding='utf-8')

#print(as_jsono(d))

assert(json.loads(json.dumps(d)) == json.loads(r"""
{
 "filename": "test/data1.csv",
 "fields": {
  "id": {
   "all": [
    "CYRILIC_TEXT",
    "DIGIT_ONLY",
    "HOST",
    "HOST_NAME_RFC1123",
    "LATIN_TEXT",
    "NUM",
    "NUM_HEX",
    "NUM_HEX_SIG",
    "NUM_OCT",
    "NUM_OCT_SIG",
    "NUM_SIG",
    "str"
   ],
   "meets": [
    "CYRILIC_TEXT",
    "DIGIT_ONLY",
    "HOST",
    "HOST_NAME_RFC1123",
    "LATIN_TEXT",
    "NUM",
    "NUM_HEX",
    "NUM_HEX_SIG",
    "NUM_OCT",
    "NUM_OCT_SIG",
    "NUM_SIG",
    "str"
   ]
  },
  "name": {
   "all": [
    "CYRILIC_ONLY",
    "CYRILIC_TEXT",
    "str"
   ],
   "meets": [
    "CYRILIC_ONLY",
    "CYRILIC_TEXT",
    "str"
   ]
  }
 }
}
"""))
