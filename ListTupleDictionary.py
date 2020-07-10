MyList1=[1,3,5,7,9]
MyList2=["cat","dog"]
MyTuple=('x','y','z','w')
MyDictionary={
    "Raj":"name",
    "Lion":"animal",
    "Peacock":"bird",
    "Pen":"object"
}


#Assigning elements to lists
MyList1.append(5)
MyList1.append(10)
print(MyList)
MyList2.append("mouse")
print(MyList2)

#Accessing elements from a tuple
print(MyTuple[2])
print(MyTuple[0])

#Deleting different dictionary elements
del MyDictionary["Pen"]
print(MyDictionary)
MyDictionary.pop("Peacock")
print(MyDictionary)
