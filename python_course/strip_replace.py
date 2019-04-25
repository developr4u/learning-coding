name, char = input("enter name and character separated by comma ").split(",")
print(f"length of {name} is",len(name))
x = char.strip()
print(f"your {char} count in {name} is",name.lower().count(x.lower()))
print(name.lower().replace("h","*"))

