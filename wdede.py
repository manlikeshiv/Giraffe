seq = [0, 1]
n = 25_997_544

while len(seq) < 100:
    x = seq[-1] + seq[-2]
    seq.append(x)

print(seq)

evennum = []

for num in seq:
    if num < n and num % 2 == 0:
        evennum.append(num)

print(evennum)

sum = sum(evennum)

print (sum)
