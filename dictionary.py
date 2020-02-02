def dict():
  thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  print(thisdict)

def accitem():
  thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  print(thisdict)
  x = thisdict["model"]

def getitem():
  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  x = thisdict.get("model")
  print(x)

def cngval():
  thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  thisdict["year"] = 2018
  print(thisdict)

def loopkey():
  thisdict =  {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  for x in thisdict:
    print(x)

def loopval():
  thisdict =  {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  for x in thisdict:
    print(thisdict[x])

def loop3():
  thisdict =  {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  for x in thisdict.values():
    print(x)

def loop4():
  thisdict =  {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  for x, y in thisdict.items():
    print(x, y)

# def checkkey():
#   thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
#   }
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")

def dictlength():
  thisdict =  {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  print(len(thisdict))

def additems():
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }
  thisdict["color"] = "red"
  print(thisdict)

def removpop():
  thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  thisdict.pop("model")
  print(thisdict)

def removepopit():
  thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  thisdict.popitem()
  print(thisdict)

def delitem():
  thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  del thisdict["model"]
  print(thisdict)

def clearitem():
  thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  thisdict.clear()
  print(thisdict)

def copydic():
  thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
  }
  mydict = thisdict.copy()
  print(mydict)

def copydict():
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

def nested1():
  myfamily = {
    "child1" : {
      "name" : "Emil",
      "year" : 2004
    },
    "child2" : {
      "name" : "Tobias",
      "year" : 2007
    },
    "child3" : {
      "name" : "Linus",
      "year" : 2011
    }
  }

def nested2():
  child1 = {
    "name" : "Emil",
    "year" : 2004
  }
  child2 = {
    "name" : "Tobias",
    "year" : 2007
  }
  child3 = {
    "name" : "Linus",
    "year" : 2011
  }

  myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
  }

print(myfamily)

def dictcondt():
  thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)

print(myfamily)  

def finalrun():
  print("Dictionary")
  dict()
  print()

  print("Accessing Items")
  accitem()
  print()

  print("Get Accessing Items")
  getitem()
  print()

  print("Change Values")
  cngval()
  print()

  print("Loop Through a Dictionary")
  loopkey()
  print()
  loopval()
  print()
  loop3()
  print()
  loop4()
  print()

  print("Check if Key Exists")
  #checkkey()
  print()

  print("Dictionary Length")
  dictlength()
  print()

  print("Adding Items")
  additems()
  print()

  print("Removing Items")
  removpop()
  print()
  removepopit()
  print()
  delitem()
  print()
  clearitem()
  print()

  print("Copy a Dictionary")
  copydic()
  print()
  copydict()

  print("Nested Dictionaries")
  nested1()
  print()
  nested2()

  print("The Dict() Constructor")
  dictcondt()
  print()

finalrun()