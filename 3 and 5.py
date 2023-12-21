n = 20
numbers = []
multiples = []

for number in range(1, n):
    numbers.append(number)

print(numbers)

for number in numbers:
    if number % 3 == 0 or number % 5 == 0:
        multiples.append(number)

print(multiples)
print(sum(multiples))
print (str(n))