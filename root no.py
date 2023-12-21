
n = input("Number please: ")

def digital_root(n):
    if len((str(n))) > 1:
        string = str(n)
        numberslist = []

        for number in string:
            numberslist.append(int(number))

        if len(str(sum(numberslist))) == 1:
            print(sum(numberslist))

        else:
            newsum = sum(numberslist)
            stringnewsum = str(newsum)
            newnumberslist = []

            for digit in stringnewsum:
                newnumberslist.append(int(digit))

                if len(str(sum(newnumberslist))) == 1:
                    print(sum(newnumberslist))


print (digital_root(n))