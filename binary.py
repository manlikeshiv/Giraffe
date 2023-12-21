
n= 10


binaryno = format(n, "b")

print(binaryno)

print(binaryno.count("1"))

binary = {}

for number in binaryno:
    if not number in binary:
        binary[number] = 1
    else:
        binary[number] += 1

print(binary["1"])