import _Module # 모듈 임포트
from _Module import add # add 함수만 사용하고 싶을 경우 
from _Module import sub # sub 함수만 사용하고 싶을 경우
from _Module import add, sub # add, sub 함수를 사용하고 싶을 경우 / *

print(add(1,2)) # add 함수만 따로 가져오므로 Module.add로 사용하지 않아도 된다.
print(sub(1,2)) # sub 함수만 따로 가져오므로 Module.sub로 사용하지 않아도 된다.
print(_Module.sub(2,3))

# 클래스, 변수를 포함한 모듈
print(_Module.PI) # 클래스 변수
moduleObject = _Module.Math() # 모듈안의 class Math 객체화
print(moduleObject.solv(2))