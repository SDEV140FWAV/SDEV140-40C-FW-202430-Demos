print(list(range(10)))

def myRange(stop=0, 
            start=0, step=1):
    rangeList = []
    if stop < start and step > 0:
        temp = stop
        stop = start
        start = temp

    count = start
    while count < stop:
        rangeList.append(count)
        count += step
    return rangeList

print(myRange(10))

print(myRange(10,20))
print(myRange(0,21,5))

print(myRange(start=5,stop=10, step=2))

def func(**args):
    print(args)

func(a=2, b=3, c=4, d=5, e=6, x=1, y=7)