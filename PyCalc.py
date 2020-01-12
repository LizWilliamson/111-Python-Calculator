# Program make a simple calculator
# This function adds two numbers 
def add(x, y):
   return x + y
# This function subtracts two numbers 
def subtract(x, y):
   return x - y
# This function multiplies two numbers
def multiply(x, y):
   return x * y
# This function divides two numbers
def divide(x, y):
   return x / y

def menu():
   print("Menu")
   print("1. Add")
   print("2. Subtract")
   print("3. Multiply")
   print("4. Divide")
   print("x to Exit")

print("-" * 75)
print("   Who needs fingers when you've got this super awesome Python Calculator")
print("-" * 75)

opc = ""
while(opc !="x"):
   menu()
   opc = input("Select an option: ")
   if(opc == "x"):
      break
   
   num1 = float(input("First number: "))
   num2 = float(input("Second number: "))

   if(opc == '1'):
      print(num1,"+",num2,"=", add(num1,num2))

   if (opc == '2'):
      print(num1,"-",num2,"=", subtract(num1,num2))
   if (opc == '3'):
      print(num1,"*",num2,"=", multiply(num1,num2))
   if (opc == '4'):
      print(num1,"/",num2,"=", divide(num1,num2))

   input("Press Enter to go back")

print("Thank you for using the awesome Python Calculator. Good Byte!")


