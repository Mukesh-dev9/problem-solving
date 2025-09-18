# Problem-1: Create a small calculator which performs operations such as Addition, Subtraction, Multiplication and Division using class.
#   Calculator inputs :> ‘a’, ‘b’ and ‘type of operation’
#   Datatype :> ‘a’ = double, ‘b’ = double, ‘type of operation’ = string

class calculator:
    def __init__(self ,a:float, b:float,operator:str):
        self.a=a
        self.b=b
        self.op=operator
    def calculate(self):
        if self.op=='addition':
            return self.a+self.b
        elif self.op=='subtraction':
            return self.a-self.b
        elif self.op=='multiplication':
            return self.a*self.b
        elif self.op=='division':
            if self.b==0:
                print("divide by zero error")
            else:
                return self.a/self.b
        else:
            print("invalid operation")
a=float(input("Enter first number"))
b=float(input("Enter second number"))
operator=str(input("Enter the operation"))
r=calculator(a,b,operator)
print('result',r.calculate(a,b,operator))


        


        