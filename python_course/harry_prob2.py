# Find factorial..
# Find the number of trailing zeros in that factorial..


num = int(input("Enter the numnber for factorial"))
fact = num
while num != 1:
   
    fact = fact * (num-1)
    num -= 1

print(fact)    

s = str(fact)
print(f"number of zeroes in factorial are {s.count('0')}")