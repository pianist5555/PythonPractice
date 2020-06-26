# hey = input("텍스트를 입력해주세요 =>")
# print(hey)
f = open("new.txt", mode='w',encoding="UTF-8") # r : 읽기모드 , w : 쓰기모드, a : 추가모드 # 쓰기모드 사용시 파일이 없으면 새로 생성, 있다면 덮어쓰기.
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

fr = open("new.txt", mode='r',encoding="UTF-8")
while True:
    line = fr.readline()
    if not line:break
    print(line)
fr.close()

fr = open("new.txt", mode='r',encoding="UTF-8")
lines = fr.readlines() # list로 반환
for line in lines:
    print("line=",line)
fr.close()

fr = open("new.txt", mode='r',encoding="UTF-8")
data = fr.read() # 문자열로 전체 내용을 돌려줌
print(data)
fr.close()

fr = open("new.txt", mode='a',encoding="UTF-8")
for i in range(11,20):
    data = "%d 번째 줄입니다.\n" %i
    fr.write(data)
fr.close() 

with open("new.txt", mode='a',encoding="UTF-8") as f: # with 구문을 벗어나는 순간 f.close()
    f.write("Life is too short, you need python")