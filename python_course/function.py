def add(a, b):
    result = a + b
    print(result)


def greater(a, b):
    if a < b:
        print(f"{b} is greater")

    else:
        print(f"{a} is greater")   


def is_palindrome(string):
      return string == string[::-1]


def fabonaci(i):
    b = 1
    a = -1
    c = a + b
    j = 1
    while j <= i:
            
        c = a + b
        print(c)
        a = b
        b = c
        j += 1
        

           