winning_number = 45
print("guess the number between 1 to 50")
user_number = int(input("enter number"))
if user_number == winning_number:
    print("**you win**")

elif user_number < winning_number:
    print("the number is higher than yours")

elif user_number > winning_number:
    print("the number is lesser than yours")

else:
    print("**you lose**")        