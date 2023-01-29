from common import *
from pprint import pprint

ciphertext = """lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt

wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi
iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m
vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd
wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr
jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii
ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh
mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb
bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd
wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr
riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"""

char_frequency_ordered = [char for char, _ in count_chars(ciphertext)]

mapping = {
    "u": "r",
    "r": "e",
    "y": "m",
    "m": "a",
    "w": "i",
    "k": "n",
    "j": "o",
    "t": "y",
    "q": "k",
    "x": "f",
    "s": "p",
    "n": "u",
    "l": "b",
    "c": "w",
    "f": "q",
    "o": "g",
    "e": "v",
    "a": "x",
}

for i, char in enumerate(char_frequency_ordered):
    if mapping.get(char, NOT_FOUND) == NOT_FOUND:
        mapping[char] = char_ordered[i]

for char in ciphertext:
    org = mapping.get(char, NOT_FOUND)
    if org == NOT_FOUND:
        print(char, end="")
    else:
        print(org, end="")

print("\n===================================")
print("key:\n===================================")
pprint(mapping)
