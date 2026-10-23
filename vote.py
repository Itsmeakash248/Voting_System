print("Welcome to voting system")
age = int(input("Enter your age: "))

if age >= 18:
  print("You are eligible for voting.")
  print("You can register as voter.")
elif age < 18:
  print("You are not eligible for voting.")
  print("You must be atleast 18 years old.")
