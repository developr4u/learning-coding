def sort(l):
	odd = []
	even = []
	for i in l:
		if i % 2 == 0:
			even.append(i)
		else:
			odd.append(i)
	combine = [odd , even]
	return combine

odd_even = [1,2,3,4,5,6,7]
print(sort(odd_even))    