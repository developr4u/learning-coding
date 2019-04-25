def common(a,b):
	empty = []
	for i in a:
		for j in b:
			if i == j:
				empty.append(i)
	return empty

input = [1,2,3,7,8,9]
intput = [10,6,5,4,3,2]
print(common(input,intput))    