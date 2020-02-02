def set01():
	thisset = {"apple", "banana", "cherry"}
	print(thisset)

def accsets():
	thisset = {"apple", "banana", "cherry"}

	for x in thisset:
	  print(x)

def accsets2():
	thisset = {"apple", "banana", "cherry"}

	print("banana" in thisset)

def addsets():
	thisset = {"apple", "banana", "cherry"}

	thisset.add("orange")

	print(thisset)

def updatesets():
	thisset = {"apple", "banana", "cherry"}

	thisset.update(["orange", "mango", "grapes"])

	print(thisset)

def lengthsets():
	thisset = {"apple", "banana", "cherry"}

	print(len(thisset))

def removeitem():
	thisset = {"apple", "banana", "cherry"}

	thisset.remove("banana")

	print(thisset)

def discarditem():
	thisset = {"apple", "banana", "cherry"}

	thisset.discard("banana")

	print(thisset)

def popitems():
	thisset = {"apple", "banana", "cherry"}

	x = thisset.pop()

	print(x)

	print(thisset)

def clearitems():
	thisset = {"apple", "banana", "cherry"}

	thisset.clear()

	print(thisset)

def delitems():
	thisset = {"apple", "banana", "cherry"}

	del thisset

	print(thisset)

def joinsets():
	set1 = {"a", "b" , "c"}
	set2 = {1, 2, 3}

	set3 = set1.union(set2)
	print(set3)

def joinupdt():
	set1 = {"a", "b" , "c"}
	set2 = {1, 2, 3}

	set1.update(set2)
	print(set1)

def setconst():
	thisset = set(("apple", "banana", "cherry"))
	print(thisset)

def finalrun():
    print("Sets")
    set01()
    print("")

    print("Access Items")
    accsets()
    print("")

    print("Access Items 2")
    accsets2()
    print("")

    print("Add Items")
    addsets()
    print("")

    print("Update Items")
    updatesets()
    print("")

    print("Get the Length of a Set")
    lengthsets()
    print("")

    print("Remove Item")
    removeitem()
    print("")

    print("Discard Items")
    discarditem()
    print("")

    print("Pop Items")
    popitems()
    print("")

    print("Clear Items")
    clearitems()
    print("")

    print("Join Two Sets")
    print("Union")
    joinsets()
    print("")

    print("Update")
    updatesets()
    print("")

    print("The set() Constructor")
    setconst()
    print("")

finalrun()

	#print("Del Items")
    #delitems()
    #print("")