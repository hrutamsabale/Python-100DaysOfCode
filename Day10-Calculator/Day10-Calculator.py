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
def calculator():
  x=float(input("Enter 1st number: "))
  continue_with_answer=True
  while continue_with_answer:
    for operation in operations:
      print(operation)
    selected_symbol=input("Choose an operation from above: ")
    y=float(input("Enter next number: "))
    selected_operation=operations[selected_symbol]
    result=selected_operation(x,y)
    print(f"{x}{selected_symbol}{y}={result}")
    x=result
    choice=input(f"Type 'y' to continue with {result} or type 'n' to reset: ").lower()
    if choice=="n":
      clear()
      calculator()
calculator()
