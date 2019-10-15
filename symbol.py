import re
regex = re.compile('[@#$%^&]')
string = "ankur gvcg  hbdh@fgjbnjdbnbfjhb jdhgbjd j$dfhg cdc7  k%nksj^bhsbkx"
# line = string.translate(None, '!@#$')
line = re.sub('[!@#$]', '', string)
symbol = regex.search(string, 1)
# string = "ankur gvcg $ hbdhcdc7 & knksjbhsbkx"
# print(symbol)
print(symbol.group_dict())
# print(type(symbol))