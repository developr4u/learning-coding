def reverse(l):
    none = []
    while len(l):
        none.append(l.pop())

    return none    

sample = list(range(1,11))
print(reverse(sample))    