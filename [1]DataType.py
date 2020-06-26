a = 5
b = 2
print("A를 b로 나눠서 나온 몫 = ",a//b) # A를 b로 나눠서 나온 몫
print("A를 b로 나눠서 나온 나머지 = ",a%b) # A를 b로 나눠서 나온 나머지
print("A를 b만큼 제곱하여 나온 값 = ",a**b) # A를 b만큼 제곱하여 나온 값

print("Python's favorite food is perl") # '를 포함하고 싶을 경우
print('"Python is very easy." he said') # "를 포함하고 싶을 경우
print('python\'s favorite food is perl') # '를 포함하고 싶을 경우 \ 활용
print("\"Python is very easy.\" he said.") # "를 포함하고 싶을 경우 \ 활용

multilineN = "Life is too short\nYou need python" # 멀티 라인 \n 활용
print("\""+multilineN+"\"")
# 멀티 라인 ''', """ 활용
multiline = '''Life is too short
You need python'''
print(multiline)

a = "python"
print(a*2) # 문자열 곱
print("len(a) = "+str(len(a))) # 문자열 길이 확인
print("a[0:3] = " + a[0:3]) #문자 인덱싱
print("a[3:] = " + a[3:]) 
print("a[:4] = " + a[:4]) 
print("a[2:-2] = " + a[2:-2]) # 2에서부터 -3까지 

print("I eat %d apples." %3) # 문자열 포맷팅
print("I eat %s apples." %"many")

number = 5
day = "three"
print("I ate %d apples. so I was sick for %s days." %(number, day)) # 복수 문자열 포맷팅
print("%10s is" %"hello") # 10개의 칸에서 오른쪽 정렬
print("%-10s is" %"hello") # 10개의 칸에서 왼쪽 정렬
print("%0.4f" %3.42134234) # 소수점 네 번째 자리만 표현
print("%10.4f" %3.42134234) # 10개의 칸에서 소수점 네 번째 자리만 표현하고 오른쪽 정렬
print("I eat {0} apples {1}".format(5,"wow!")) # 순서
print("I eat {number} apples {text} ".format(number = 5,text = "wow!")) # name
print("\"{0:<10}\"".format("hi")) # 10개의 칸에서 왼쪽 정렬
print("\"{0:>10}\"".format("hi")) # 10개의 칸에서 오른쪽 정렬
print("\"{0:^10}\"".format("hi")) # 10개의 칸에서 가운데 정렬
print("\"{0:10.4f}\"".format(3.42134234)) # 10개의 칸에서 소수점 네 번째 자리만 표현하고 오른쪽 정렬 똑같은 표현식 사용 가능
print("{{ dictionary }}".format()) # {}를 그대로 사용하고 싶을 경우
print(f"오늘은 {number+1}개의 사과를 먹어야겠다.") # python 3.6이상 f 문자열 포매팅 기능 사용가능

dictions = {'name' : '홍길동', 'age' : 10}
print(f'나의 이름은 {dictions["name"]}입니다. 나이는 {dictions["age"]}입니다.')  # python 3.6이상 f 문자열 포매팅 기능에서는 딕셔너리를 이런식으로 사용 할 수 있다.
print(f'{"hi":!^10}') # 공백채우기 정렬 10개의 칸에서 가운데정렬하고 남은 공간은 !로 채워라

hobbyName = 'hobby'
print("hobbyName.count('b') = "+str(hobbyName.count('b'))) # 문자 개수 확인 count 함수
print(hobbyName.find('b')) # 문자가 처음나오는 인덱스를 알려주는 find 함수 없으면 -1을 반환 index 함수도 있지만 없다면 예외를 발생함
print('!'.join(['d','a','b'])) # 리스트나 튜플에도 사용가능 !로 합침
print(hobbyName.upper()) # 대문자
print(hobbyName.lower()) # 소문자

trimName = ' trim:Ar'
print(trimName.lstrip()) # 왼쪽 공백 삭제, rstrip() 오른쪽 공백 삭제, strip() 양쪽 공백 삭제
print(trimName.replace("trim", "strip")) # 문자열 교체 replace()
print(trimName.split(':')) # 문자열 나누기 :기준, split()일 경우 공백 기준