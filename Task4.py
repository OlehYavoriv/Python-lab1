user=(input("Enter your name:"))
print("Welcome" , user, "!")
chyslo1=float(input("Enter first number:"))
chyslo2=float(input("Enter second number:"))
diya=str(input("Enter (+,-,*,/):"))
if diya == "/" and chyslo2 == 0:
        print("You cannot divide by zero!")
        exit()
if diya == "+":
   print("Result:",chyslo1+chyslo2)
elif diya =="-":
  print("Result:",chyslo1-chyslo2)
elif diya =="*":
   print("Result:",chyslo1*chyslo2)
elif diya =="/":
    print("Result:",chyslo1/chyslo2)
else:
    print("Error!")