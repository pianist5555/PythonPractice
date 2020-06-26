t = True
f = False
print(type(t))
print(1!=1)
number_t=[1,2,3,4] # 숫자형은 0 이 아니면 True / list는 []가 아니면 True , None은 거짓
while number_t:
    print(number_t.pop(),len(number_t))
print(bool('')) # 내장 함수 bool로 T/F 판별 가능