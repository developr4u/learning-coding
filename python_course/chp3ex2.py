print("please get permission to watch movie")
user_name = input("Enter your name ")
user_age = int(input("Enter your age "))

if user_name.lower()[0] == "a":
    if user_age >=10:
        print("you are allowed to watch movie")

    else:
        print("your age is not suitable to watch")

else:
    print("your name is not in list, you cant")            