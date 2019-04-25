def sublist_count(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count


input = [1,2,3,[4,5,6],[7,8,9]]
print(sublist_count(input))