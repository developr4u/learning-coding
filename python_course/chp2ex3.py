name, ch = input("enter a name and a character separated by comma ").split(",")
print(f"length of your {name} is",len(name))
name.lower().count(ch.lower())
print("your character count is",name.lower().count(ch.lower()))