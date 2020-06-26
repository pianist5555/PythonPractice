try:
    a = [1, 2]
    print(a[3])
    4 / 0
except (ZeroDivisionError, IndexError) as e: # 먼저 발생되는 오류만 예외 발생
    print(e)
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

try:
    f = open('new.txt',mode='w')
finally: # 무조건 수행
    f.close()

try:
    f = open('zero.txt', mode='r')
except FileNotFoundError: # 에러가 발생해도 통과시켜야 할 경우
    pass

class TestModule:
    testOne = 1
class Test(TestModule):
    def raised(self):
        raise NotImplementedError # 예외를 발생
test = Test()
test.raised()

class MyError(Exception): # 예외 만들기
    def __str__(self):
        return '허용되지 않는 별명입니다.'

def say_nick(nick):
    if nick == 'pool':
        raise MyError()
    print(nick)

try:
    say_nick('yellow')
    say_nick('pool')
except MyError as e:
    print(e)