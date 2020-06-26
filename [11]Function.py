def add(a,b):
    result = a + b
    return result
c = add(1,2)
print(c)
print(add(2,3))
print(add(b=5,a=2)) # 매개변수명 지정

def printAdd(a,b): # 결과 값이 없는 함수
    print("%d와 %d를 받아서 %d를 프린트했다." %(a,b,a+b))
printAdd(1,5)

def add_many(*args): # 복수의 입력값
    result = 0
    print(type(args)) # tuple로 넘어옴
    for i in args:
        result = result + i
    return result
print(add_many(1,2,3,4,5,6))

def add_mul(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result += i 
        return result
    elif choice == 'mul':
        result = 1 
        for i in args:
            result *= i 
        return result
print(add_mul('add',1,2,3,4), add_mul('mul',1,2,3,4))

def print_kwargs(**kwargs): # 키워드 파라미터를 사용하면 딕셔너리 객체를 생성하여 받아옴
    if kwargs.get('name') == 'foo':
        print("나의 이름은 %s야!" %kwargs.get('name'))
    print(kwargs)
print_kwargs(a=1,b=2,name='foo')

def add_and_mul(a,b):
    return a+b, a*b
resultMulOne = add_and_mul(2,3) # 튜플로 생성되어 대입
print(resultMulOne)
resultMulTwo, resultMulThree = add_and_mul(3,4) # 동적 할당
print(resultMulTwo,resultMulThree)

def defaultDef(a,b=5,c=True): # 디폴트의 파라미터 위치는 뒤에 있어야 함
    print(a,b,c)
defaultDef('haha')

add = lambda a, b : a+b # lambda 매개변수, 매개변수, .. : 표현식 / # js 와 비교: const add = (매개변수) => {표현식}
result = add(2,3)
print(result)