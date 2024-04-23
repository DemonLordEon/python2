word = input("trap a word""\n")

space = int(input("chssoe""\n"))

length = len(word)

spaceamount = length + space *2

box = ""

box += "#" * (spaceamount + (1*2))
box += "\n"
box += "#" + " " * spaceamount + "#"
box += "\n"
box += "#" + " " * spaceamount + "#"
box += "\n"
box += "#" + " " * spaceamount + "#"
box += "\n"
box += "#" * (spaceamount + (1*2))

print(box)