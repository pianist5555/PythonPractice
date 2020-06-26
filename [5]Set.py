set_one = set([1,2,3])
set_oneJoin = set([2,3,4,5])
set_two = set('HelloWorld!') # 중복을 허용하지 않는다, 순서가 없다, 순서가 없기 때문에 인덱싱으로 값을 얻을 수 없다.
print(set_one, set_two)
set_two_list = list(set_two)
print(set_two_list[0]) # 리스트로 바꿔서 인덱싱

print(set_one & set_oneJoin) # 교집합 or set_one.intersection(set_oneJoin)
print(set_one | set_oneJoin) # 합집합 or set_one.union(set_oneJoin), 중복 x
print(set_one - set_oneJoin) # 차집합 or set_one.difference(set_oneJoin)

set_one.add(7) # 요소 1개 추가
set_one.update([8,9]) # 요소 여러개 추가
print(set_one)
set_one.remove(3) # 요소 삭제
print(set_one) 