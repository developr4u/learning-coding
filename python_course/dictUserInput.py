user_info = {}
user_info['name'] = input("Enter your name: ")
user_info['age'] = input("Enter your age: ")
user_info['fav songs'] = input("Enter your fav songs separated by comma : ").split(",")
user_info['fav movies'] = input("Enter your fav movies: ").split(",")

for key,value in user_info.items():
    print(f"{key}:{value}")
