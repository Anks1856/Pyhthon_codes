anks = "ankur is a coder .He have a # good $ knowladge of 4 to 5 programming language.He alsohave good knowladgeof 4 language."

Int = [int(i) for i in anks.split() if i.isdigit()]
# Symbol = [Symbol(i) for i in anks.split() if i.isprintable()]

print(Int)
# print(Symbol)