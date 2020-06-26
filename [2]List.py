number = [1,2,3]
meltNumber = [1,2,3,['a','b','c']]
print(f'number[0]+number[1] = {number[0]+number[1]}') # 리스트 연산 1
print(number+meltNumber) # 리스트 연산 2
print(meltNumber*3) # 리스트 반복
print(number[-1]+number[-2])
print(meltNumber[-1][0]) # 이중 리스트
print(meltNumber[0:2]) # 리스트 슬라이싱
print(meltNumber[:2]) # 처음부터 <2까지
print(meltNumber[2:]) # 2부터 끝까지
print(len(number))
number[0] = 5 # 문자열은 값을 수정하거나 삭제할 수 없지만 리스트는 가능
print(number)
del number[1:] # 문자열의 인덱스 1부터 끝까지 삭제
print(number)

numberF = [1,6,3]
numberF.append(4) # 마지막 인덱스 +1 에 요소 추가
numberF.insert(0,9) # 0번째 인덱스에 9라는 요소 추가
numberF.remove(1) # 순차적으로 검색하여 이 나오면 지워라. 한 개만 지워집니다.
numberIsPop = numberF.pop() # 제일 위에 쌓여있는 요소를 꺼낸다.
print("numberIsPop = "+str(numberIsPop))
numberF.append(['f','a','b'])
print(numberF) 
del numberF[3]
numberF.sort()
print(numberF) # 문자도 sort 가능
numberF.reverse()
print(numberF) # 역순으로 정렬
print(numberF.index(3)) # 3이 있는 인덱스를 반환
print(numberF.count(3)) # 3이 몇개 있는지 총량을 반환
numberExtend = [7,7]
numberF.extend(numberExtend) # 리스트 2개 연산 numberF += [7,7]과 같다.
print(numberF)