user_input = input("Enter a number: ")
i = 0
total = 0
length = len(user_input)
while length > 0:
    total = int(user_input[i]) + total
    length -= 1
    i += 1
print(total)    
     