#if
a = 33
b = 200
if b > a:
  print("b is greater than a")

#if-else
#   
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

#if-elif-else

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
