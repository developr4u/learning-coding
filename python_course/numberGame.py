import random
print('''
           ***
               "WELCOME TO NUMBER GAME"
                                       ***''')
user_input = int(input("Guess the Number: "))
i = 1
winning_number = random.randint(1,100)
while i<10:
                
    if user_input == winning_number:
        print('''******You Won!!******
        ******''')
        print(f"You Tried {i} Times")
        break                                                 
    elif user_input > winning_number:
        print("Your Number is Higher than Winning Number ")
        user_input = int(input("Guess Again: "))
        i += 1

    elif user_input < winning_number:
        print("Your Number is Lower than Winning Number")
        user_input = int(input("Guess Again: "))
        i += 1

print("***THE END!!***")        
           
                                                                      