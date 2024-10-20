from replit import clear
def add(num1,num2):
  return num1+num2
def sub(num1,num2):
  return num1-num2
def mul(num1,num2):
  return num1*num2
def div(num1,num2):
  return num1/num2
operations={
  "+":add,
  "-":sub,
  "*":mul,
  "/":div,
}
to_continue=True
while to_continue:
  x=float(input("Enter 1st number: "))
  for operation in operations:
    print(operation)
  reset=False
  while not reset:
    operation=input("Choose an operation: ")
    chosen_operation=operations[operation]
    y=float(input("Enter 2nd number: "))
    result=chosen_operation(x,y)
    print(f"{x}{operation}{y}={result}")
    choice=input(f"\nType 'y' to continue with {result}, 'n' to reset, 'e' to exit: ").lower()
    if choice=="e":
      print("\nEXITING................")
      reset=True
      to_continue=False
    elif choice=="n":
      clear()
      reset=True
    elif choice=="y":
      x=result
