def func01():
    def my_function():
      print("Hello from a function")

    my_function()

def func02():
    def my_function(fname):
        print(fname + " Refsnes")

    my_function("Emil")
    my_function("Tobias")
    my_function("Linus")

def func03():
    def my_function(country="Norway"):
        print("I am from " + country)

    my_function("Sweden")
    my_function("India")
    my_function()
    my_function("Brazil")

def func04():
    def my_function(food):
        for x in food:
            print(x)

    fruits = ["apple", "banana", "cherry"]

    my_function(fruits)

def func05():
    def my_function(x):
        return 5 * x

    print(my_function(3))
    print(my_function(5))
    print(my_function(9))

def func06():
    def my_function(child3, child2, child1):
        print("The youngest child is " + child3)

    my_function(child1="Emil", child2="Tobias", child3="Linus")

def func07():
    def my_function(*kids):
        print("The youngest child is " + kids[2])

    my_function("Emil", "Tobias", "Linus")

def func08():
    def tri_recursion(k):
        if (k > 0):
            result = k + tri_recursion(k - 1)
            print(result)
        else:
            result = 0
        return result

    print("\n\nRecursion Example Results")
    tri_recursion(6)

def finalrun():
    print("Creating and Calling A Function")
    func01()
    print()

    print("Parameters")
    func02()
    print()

    print("Default Parameter Value")
    func03()
    print()

    print("Passing a List as a Parameter")
    func04()
    print()

    print("Return Value")
    func05()
    print()

    print("Keyword Arguments")
    func06()
    print()

    print("Arbitrary Arguments")
    func07()
    print()

    print("Recursion")
    func08()
    print()

finalrun()