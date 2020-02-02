def list1():
    thislist = ["apple", "banana", "cherry"]
    print(thislist)

def accesitem():
    thislist = ["apple", "banana", "cherry"]
    print(thislist[1])

def negativeindex():
    thislist = ["apple", "banana", "cherry"]
    print(thislist[-1])

def rangeindex():
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[2:5])

def rangeneg():
    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[-4:-1])

def changeitem():
    thislist = ["apple", "banana", "cherry"]
    thislist[1] = "blackcurrant"
    print(thislist)

def loopthrough():
    thislist = ["apple", "banana", "cherry"]
    for x in thislist:
        print(x)

def checkif():
    thislist = ["apple", "banana", "cherry"]
    if "apple" in thislist:
        print("Yes, 'apple' is in the fruits list")

def listlength():
    thislist = ["apple", "banana", "cherry"]
    print(len(thislist))

def additems():
    thislist = ["apple", "banana", "cherry"]
    thislist.append("orange")
    print(thislist)

def additems2():
    thislist = ["apple", "banana", "cherry"]
    thislist.insert(1, "orange")
    print(thislist)

def rmvitem():
    thislist = ["apple", "banana", "cherry"]
    thislist.remove("banana")
    print(thislist)

def rmvitem2():
    thislist = ["apple", "banana", "cherry"]
    thislist.pop()
    print(thislist)

def rmvitem3():
    thislist = ["apple", "banana", "cherry"]
    del thislist[0]
    print(thislist)

def rmvitem4():
    thislist = ["apple", "banana", "cherry"]
    del thislist

def rmvitem5():
    thislist = ["apple", "banana", "cherry"]
    thislist.clear()
    print(thislist)

def copylist():
    thislist = ["apple", "banana", "cherry"]
    mylist = thislist.copy()
    print(mylist)

def copylist2():
    thislist = ["apple", "banana", "cherry"]
    mylist = list(thislist)
    print(mylist)

def joinlist():
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]

    list3 = list1 + list2
    print(list3)

def joinlist2():
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]

    for x in list2:
        list1.append(x)

    print(list1)

def joinlist3():
    list1 = ["a", "b", "c"]
    list2 = [1, 2, 3]

    list1.extend(list2)
    print(list1)

def listconstruct():
    thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
    print(thislist)

def tuple1():
    thistuple = ("apple", "banana", "cherry")
    print(thistuple)

def tupleitems():
    thistuple = ("apple", "banana", "cherry")
    print(thistuple[1])

def negidx():
    thistuple = ("apple", "banana", "cherry")
    print(thistuple[-1])

def rangeidx():
    thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
    print(thistuple[2:5])

    print(thistuple[-4:-1])

def changetuple():
    x = ("apple", "banana", "cherry")
    y = list(x)
    y[1] = "kiwi"
    x = tuple(y)

    print(x)

def looptuple():
    thistuple = ("apple", "banana", "cherry")
    for x in thistuple:
        print(x)

def checktuple():
    thistuple = ("apple", "banana", "cherry")
    if "apple" in thistuple:
        print("Yes, 'apple' is in the fruits tuple")

def tuplelength():
    thistuple = ("apple", "banana", "cherry")
    print(len(thistuple))

def createonetuple():
    thistuple = ("apple",)
    print(type(thistuple))

    # NOT a tuple
    thistuple = ("apple")
    print(type(thistuple))

def removetuple():
    thistuple = ("apple", "banana", "cherry")
    del thistuple
    print(thistuple)

def jointuple():
    tuple1 = ("a", "b", "c")
    tuple2 = (1, 2, 3)

    tuple3 = tuple1 + tuple2
    print(tuple3)

def tupleconst():
    thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
    print(thistuple)

def finalrun():
    print("List")
    list1()
    print("")

    print("Access Item")
    accesitem()
    print("")

    print("Negative Indexing")
    negativeindex()
    print("")

    print("Range of Indexes")
    rangeindex()
    print("")

    print("Range of Negative Indexes")
    rangeneg()
    print("")

    print("Change Item Value")
    changeitem()
    print("")

    print("Loop Through a List")
    loopthrough()
    print("")

    print("Check If Item Exists")
    checkif()
    print("")

    print("List Length")
    listlength()
    print("")

    print("Add Items")
    additems()
    print("")
    additems2()
    print("")

    print("Remove Item")
    rmvitem()
    print("")
    rmvitem2()
    print("")
    rmvitem3()
    print("")
    rmvitem4()
    print("")
    rmvitem5()
    print("")

    print("Copy a List")
    copylist()
    print("")
    copylist2()
    print("")

    print("Join List")
    joinlist()
    print()
    joinlist2()
    print()
    joinlist3()
    print()

    print("The List Constructor")
    listconstruct()
    print()

finalrun()

def tuplerun():
    print("TUPLE")
    tuple1()
    print()

    print("Access Tuple Items")
    tupleitems()
    print()

    print("Negative Indexing")
    negidx()
    print()

    print("Range of Indexes")
    rangeidx()
    print()

    print("Change Tuple Values")
    changetuple()
    print()

    print("Loop Through a Tuple")
    loopthrough()
    print()

    print("Check if Item Exists")
    checktuple()
    print()

    print("Tuple Length")
    tuplelength()
    print()

    print("Create Tuple With One Item")
    createonetuple()
    print()

    print("Remove Items")
    removetuple()
    print()

    print("Join Two Tuple")
    jointuple()
    print()

    print("The Tuple Constructor")
    tupleconst()
    print()

#tuplerun()