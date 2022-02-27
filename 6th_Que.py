# 6)-Write a Python class called Calculator by completing the tasks below:
class Calculator(object):
    def __init__(self,num1 , num2):
        self.num1 = num1
        self.num2 = num2

    def Add(self):
        return print(self.num1 + self.num2)

    def Subtract(self):
        return print(self.num2 - self.num1)

    def Multiply(self):
        return print(self.num1 * self.num2)

    def Divide(self):
        return print(self.num2 / self.num1)

Obj = Calculator(10,94)
Obj.Add()
Obj.Subtract()
Obj.Multiply()
Obj.Divide()