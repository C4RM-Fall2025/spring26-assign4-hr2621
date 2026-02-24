

def FizzBuzz(start, finish):
    
    outlist = []

    i = start
    while i <= finish:

        if i % 15 == 0:
            outlist.append("fizzbuzz")

        elif i % 3 == 0:
            outlist.append("fizz")

        elif i % 5 == 0:
            outlist.append("buzz")

        else:
            outlist.append(i)

        i = i + 1

    return(outlist)
