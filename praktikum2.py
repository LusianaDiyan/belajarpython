def ifelse():
    a = 33
    b = 200
    if b > a:
      print("b is greater than a")

def elif01():
    a = 33
    b = 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")

def else01():
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
    else:
        print("a is greater than b")

def else02():
    a = 200
    b = 33
    if b > a:
        print("b is greater than a")
    else:
        print("b is not greater than a")

def shorthandif1():
    a = 200
    b = 33
    if a > b: print("a is greater than b")

def shorthand02():
    a = 2
    b = 330
    print("A") if a > b else print("B")

    a = 330
    b = 330
    print("A") if a > b else print("=") if a == b else print("B")

def and01():
    a = 200
    b = 33
    c = 500
    if a > b and c > a:
        print("Both condition are True")

def or01():
    a = 200
    b = 33
    c = 500
    if a > b or a > c:
        print("At least one of the condition is True")

def nestedif():
    x = 41

    if x > 10:
        print("Above ten, ")
        if x > 20:
            print("and also above 20!")
        else:
            print("but not above 20.")

    a = 50
    b = 10
    if a > b:
        print("Hello World")

def whileloop():
    i = 1
    while i < 6:
        print(i)
        i +=1

def breakstat():
    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break
        i += 1

def constat():
    i = 0
    while i < 6:
        i += 1
        if i == 3:
            continue
        print(i)

def elsestat():
    i =1
    while i < 6:
        print(i)
        i += 1
    else:
        print("i is no longer less than 6")

def forloop1():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)

def loopstring():
    for x in "banana":
        print(x)

def breakstat():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)
        if x == "banana":
            break

def breakstat2():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        if x == "banana":
            break
        print(x)

def constat():
    fruits = ["apple", "banana", " cherry"]
    for x in fruits:
        if x == "banana":
            continue
        print(x)

def rangefunc():
    for x in range(6):
        print(x)

    for x in range(2, 6):
        print(x)

    for x in range(2, 30, 3):
        print(x)

def elseforloop():
    for x in range(6):
        print(x)
    else:
        print("Finally finished!")

def nestedloop():
    adj = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]

    for x in adj:
        for y in fruits:
            print(x, y)

    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)

def finalrun():
    print("IF Statement")
    ifelse()
    print("\n")

    print("ELIF")
    elif01()
    print()

    print("ELSE")
    else01()
    print()

    print("ELSE 2")
    else02()
    print()

    print("Short Hand If")
    shorthandif1()
    print()

    print("Short Hand If.. Else")
    shorthand02()
    print()

    print("And")
    and01()
    print()

    print("OR")
    or01()
    print()

    print("Nested If")
    nestedif()
    print()

    print("While Loop")
    whileloop()
    print()

    print("Break Statement")
    breakstat()
    print()

    print("Continue Statement")
    constat()
    print()

    print("Else Statement")
    elsestat()
    print()

    print("For Loops")
    forloop1()
    print()

    print("Looping Through a String")
    loopstring()
    print()

    print("Break Statement")
    breakstat()
    print()
    print("Break Statement 2")
    breakstat2()
    print()

    print("Continue Statement")
    constat()
    print()

    print("Range Function")
    rangefunc()
    print()

    print("Else in For Loop")
    elseforloop()
    print()

    print("Nested Loops")
    nestedloop()
#finalrun()



