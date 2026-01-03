fruits = {"Apple", "Banana", "Mango", "Orange"}
print(fruits)

print(type(fruits)) #shows datatype

fruits.add("Grapes") #add element 
print(fruits)

fruits.remove("Banana") #remove element
print(fruits)

print(len(fruits)) #length

print("Apple" in fruits) #check element
print("Pineapple" in fruits)

for fruit in fruits: 
    print(fruit) #types elements of fruits

#lets define more sets
set1 = {"Chaitany", "Aditya", "Sanket"}
set2 = {"Sanket", "Pritam", "Sagar"}

print(set1 | set2) #union

print(set1 & set2) #intersection

print(set1 - set2) #difference
