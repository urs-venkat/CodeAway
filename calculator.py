#Taking operands asinput from user

operand1=int(input("Please enter first number"))

operand2=int(input("Thank you ! kindly please enter next number"))

#Taking operator from user

operator=input("Enter any one of(+,-,*,/,%) to perform calculation on the given njumbers")

#  if elif ladder  for calculation
 
# using match condition  for calculations
# which make ease than if else ladder
match operator:

     #Addition
     
     case "+":
          sum=operand1+operand2
          print("Addition of",operand1,"and",operand2,"is",sum)
     
     #Subtraction
     
     case "-":
          subtraction=operand1-operand2
          print("Subtraction of",operand1,"from",operand2,"is",subtraction)

     #multiplication
     
     case "*":
          product=operand1*operand2
          print("Product of",operand1,"and",operand2,"is",product)
     
     #Division
     
     case "/":
          division=operand1/operand2
          print("Division between",operand1,"and",operand2,"is",division)
     
     #Remainder
     
     case "%":
          remainder=operand1%operand2
          print("Remaoinder is",remainder)

     
     #Default case
     case _:
          print("Entered Invalid operator")







 
