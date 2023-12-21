paren_str = "((()))"

while len (paren_str) > 2:
    paren_str = paren_str.replace("()","")


print(paren_str)

if paren_str == "()":
    print(True)
