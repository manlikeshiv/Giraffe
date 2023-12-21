n = input("Number please: ")

def no_boring_zeros(n):

    if int(n) == 0:
        return 0

    else:

        if int(n) < 0:
            m = int(n) * -1

        else:
            m = n

        string = str(m)
        numberslist = []

        for number in string:
            numberslist.append(int(number))

        while numberslist[-1] == 0:
            numberslist = numberslist[:-1]

        else:
            boring0removed = ''.join(str(num) for num in numberslist)
            if int(n) < 0:
                return int(boring0removed) * -1
            else:
                return int(boring0removed)







print (no_boring_zeros(n))