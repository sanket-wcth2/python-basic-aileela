#while loop

i = 1 # initalize value of i
while i <= 5: #will go in loop till x value is less or equals to 5
    print(i)
    i += 1 # x = x + 1

#while loop for infinite inputs until specfic word is said it stops

while True:
    name = input('Input name: ')
    if name == 'stop':
        break
    print("Your name is:", name)

#while looop with if staement

i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i += 1

#simple program for chocies with while loop 
#also conditional satements

choice = 0

while choice != 3:
    print("\nMENU")
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a + b)

    elif choice == 2:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a - b)

    elif choice == 3:
        print("Exiting program...")

    else:
        print("Invalid choice")
