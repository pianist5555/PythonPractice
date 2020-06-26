d_one = {'a' : [1,2,3]} 
print(d_one['a'])
d_one['b'] = [4,5,6] # 쌍추가
d_one[1] = 'font'
print(d_one)

del d_one['b'] # 쌍삭제
print(d_one)
print(d_one.keys()) # key값을 모아서 dict_keys 객체로 돌려줌
print(list((d_one.keys()))) # List로 사용하기 위해 형변환 // 리스트의 고유 함수를 사용하기 위한 캐스팅
print(list(d_one.values())) # value값을 모아서 돌려줌
print(d_one.items()) # key,value를 dict_keys 객체로 돌려줌
print("d_one.get('a') = "+str(d_one.get('a'))) # ket로 value 가져오기 // a가 없을경우 None을 리턴함
print(d_one.get('d','그런건없어!')) # key값이 없으면 디폴트 값을 발생
print(d_one['a']) #  d_one['a']도 가능하지만 key가 없을 경우 예외를 발생
print('a' in d_one) # key값이 존재하나요?
d_one.clear() # 쌍 모두 지우기
print(d_one)