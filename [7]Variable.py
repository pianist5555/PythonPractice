variable_a = [1,2,3]
print(id(variable_a)) # 객체의 주소
variable_b = variable_a
print(id(variable_b)) # passed by assignment
print(variable_a is variable_b)
variable_a = [1,2,3,4] # 주소가 바뀌었지만
print(id(variable_b)) # b의 주소는 그대로
print(id(variable_a)) # a는 변경됨

variable_c = variable_a[1:] # 자르기 가능
print(variable_c)

from copy import copy # copy module 사용하기
variable_d = copy(variable_a)
print("variable_d = " + str(variable_d))

variable_e, variable_f = ('python', 'variable') # 1번째 방법
print(variable_e, variable_f)

(variable_g, variable_h) = 'python2', 'variable2' # 2번째 방법
print(variable_g, variable_h)

[variable_i, variable_j] = ['python3','variable3'] # 3번째 방법
print(variable_i,variable_j)

variable_k = variable_l = 'python4' # 복수의 변수에 동일한 값 대입
print(variable_k, variable_l)

variable_e, variable_f = variable_f, variable_e # 자리 바꾸기
print(variable_e, variable_f)