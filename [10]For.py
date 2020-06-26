test_list = ['one', 'two', 'three']
for i in test_list: # 조건문 in과 다름. 
    print(i)

plus_list = [(1,2),(3,4),(5,6)]
for (first) in plus_list:
    print(first)
for (first, last) in plus_list:
    print(first + last)

range_number = range(10) # 0부터 10 미만의 숫자를 포함하는 range 객체를 만들어준다.
print(range_number)
range_number_re = range(1,11) # 1부터 11 미만의 숫자를 포함하는 range 객체를 만들어준다.
print(range_number_re)

add = 0
for i in range(1,10):
    add +=1
print(add)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue
    print("%d번 학생 축하합니다." %(number+1))

vector = [1,2,3,4]
result = []
for i in vector:
    result.append(i*3)
print(result)    
result_two = [num * 4 for num in vector if num & 3 == 0] # [표현식(변수) for 변수 in 반복 가능 객체 if 조건]
print(result_two)

result_doble = [x*y for x in range(10) if x > 0
                    for y in range(10) if y > 0] # for 2개 이상
print(result_doble)