
seq = [8, 4, 14, 10, 3, 14, 14, 10, 3, 4, 10, 14, 4, 7, 3, 3, 7, 4, 4, 10, 10, 4, 8, 10, 3, 14, 14]

numbercount = {}

for number in seq:
    if number not in numbercount:
        numbercount[number] = 1
    else:
        numbercount[number]+=1

for number in numbercount:
    if (numbercount[number])%2 == 1:
        print(number)

print (numbercount[4])
print(numbercount)