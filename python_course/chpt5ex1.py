def sqr_fun(l):
    empty_l = []
    for i in l:
        empty_l.append(i**2)
    return empty_l    


var = list(range(1,11))
print(sqr_fun(var))