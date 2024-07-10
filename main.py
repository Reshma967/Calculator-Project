def calculator():
    def add(a,b):
        return a+b
    def subtract(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        return a/b
    operations={
        "+":add,
        "-":subtract,
        "*":multiply,
        "/":divide
    }
    num1=int(input("enter first number:"))
    for sym in operations:
        print(sym)
    ass=True
    while ass:
        pick=input("Pick symbol:")
        num2=int(input("enter next number:"))
        calc=(operations[pick](num1,num2))
        print(f"{num1} {pick} {num2} = {calc}")
        repeat=input(f"Type y to continue calculating with {calc} or type n to exit")
        if(repeat=="n"):
            ass=False
            print("the end")
            calculator()
        else:
            num1=calc
           
           
calculator()

