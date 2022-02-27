# 5) Question
totalmarks = 0
class Question(object):
    def __init__(self):
        self.name = 'mark'
        self.phy = 80
        self.chem = 90
        self.bio = 40


    def total(self):
        totalmarks = 80 + 90 + 40
        return totalmarks


    def percentage(self):
        a = (self.total()/300)*100
        return print((a))


Obj = Question()
Obj.total()
Obj.percentage()