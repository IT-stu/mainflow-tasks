"""
Mukesh
            Task-1
Basic Data types in Python
"""
#List: Mutable,Ordered,Allow Duplicate
#Create a list
My_list=["Mukesh","Kumar","Rohit","Mohan"]
print("Create a List ",My_list )

#Slicing a List
print("Slicing ",My_list[0:4])

#Adding a List
My_list.append("Senthil")
print("Adding a List ",My_list)

#Removing Specific Element on List 
My_list.remove("Mukesh")
print("Removing Specific Element ",My_list)

#Removing With index Value on List if Parameter is not Given on pop it Defaultly Delete the last element
My_list.pop()
print("Removing One element",My_list)

#Modifying Element on list
My_list[0]="Saravanan"
print("Modifying Element ",My_list)

#Clear the all Element in python
My_list.clear()
print("Clear the all Element ",My_list)

#Delete the Variable
del My_list

#--------------------------------------------------------------

#Tuple:immutable,Ordered
#Create a Tuple
My_tuple=("Mukesh","Kumar","Rohit","Mohan")
print("Create a Tuple ",My_tuple)

#Slicing a tuple
print("Slicing a tuple ",My_tuple[0:4])

#Concatenating 2 Tuples
Tuple1 = (0, 1, 2, 3)
Tuple2 = ('One', 'Two')
print(f"Concatenating 2 Tuples {Tuple2} + {Tuple2}")

#Nested Tuples
Tuple3 = (Tuple1, Tuple2)
print("Nested Tuples",Tuple3)

#Length in Tuple
print("Length in Tuple ",len(My_tuple))

# Repetition in Tuples
print("Repetition in Tuples ",Tuple1*3)

#Delete the Variable
del My_tuple

#_____________________________________________________________________________


#Set: Mutable,Unordered, Duplicate
#Create a Set
My_set={"Mukesh","Kumar","Rohit","Mohan"}
print("Create a Set :",My_set)
#Adding a set
My_set.add("Manoj") #single element to the set.
print(" Assign single element to the set :",My_set)

#Removing Specific Element on set 
My_set.remove("Mukesh")
print("Removing Specific Element on set :",My_set)
My_set.discard("Vetri")# Removes a specific element from the set without raising an error if the element is not found

#pop it Defaultly Delete the last element
My_set.pop()
print("Delete the last element :",My_set)

#Clear the all Element in python
My_set.clear()
print("Clear the all Element :",My_set)
#Delete the Variable
del My_set


#-------------------------------------------------------------
#Dictionaries

#Creating and Using Dictionaries
My_dict = {
"School": "SVGV",
"Class": "XI",
"Year": 2019
}
print("Creating and Using Dictionaries :",My_dict)

#Accessing Dictionary
print("Accessing Dictionary :",My_dict["Class"])

#Adds a new key-value pair
My_dict["Section"] = "D"
print("",My_dict)

#Modifying
My_dict["Year"] = 2020
print("Modifying :",My_dict)

#Returns the value for the specified key, or None if the key is not found.
My_dict.get("Year") 
print("Returns the value for the specified key :",My_dict)

#Returns a view object with key-value pairs as tuples.
My_dict.items()
print("Dictonary Returns a view object with key-value pairs as tuples : ",My_dict)

# Returns a view object with all the keys in the dictionary.
My_dict.keys()
print("Returns a view object with all the keys in the dictionary :",My_dict)

# Returns a view object with all the values in the dictionary.
My_dict.values()
print("Returns a view object with all the values in the dictionary :",My_dict)

#Empties the dictionary.
My_dict.clear()
print("Empties the dictionary :",My_dict)

#Deleted the Variable
del My_dict
