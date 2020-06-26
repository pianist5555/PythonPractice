class FourCal:
    def __init__(self, first, second): # __init__ 생성자 self parameter = this
        self.first = first # a.first = first
        self.second = second # a.second = second
    def setData(self, first, second):
        self.first = first 
        self.second = second 
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        return self.first * self.second
    def sub(self):
        return self.first - self.second
    def div(self):
        return self.first / self.second

a = FourCal(4,2) # init attribute
a.setData(8,7)
print(a.first, a.second, a.add(), a.mul(), a.sub(), a.div())

class MoreFourCal(FourCal): # 상속
    def pow(self):
        result = self.first ** self.second
        return result
    def div(self): # override
        if self.second == 1:
            return "Why you div this?"
        else:
            return self.first / self.second

b = MoreFourCal(4,1)
print(b.first, b.second, b.add(), b.mul(), b.sub(), b.div(), b.pow())

class Family:
    lastname = 'kim' # 클래스 변수

print(Family.lastname)
c = Family()
print(c.lastname)
Family.lastname = 'park' # 클래스 변수를 수정하면 객체들의 클래스 변수들도 수정된다.
print(c.lastname, Family.lastname)