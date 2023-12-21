
n = 5

def powerof4(n):

    if isinstance(n, int):

        if n ==1:
            return (True)

        else:
            if n % 4 != 0:
                return (False)

            else:
                while n >= 4 and n % 4 == 0:
                    n = n/4

            if n == 1:
                return (True)
            else:
                return (False)

    else:
        return (False)

print(powerof4(n))