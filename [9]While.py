treeHit = 0
while treeHit < 10:
    treeHit +=1
    print("나무를 %d번 찍습니다." %treeHit)
else :
    print("나무가 쓰러집니다.")

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d입니다." %coffee)
    if coffee == 0:
        print("커피가 떨어졌습니다. 판매를 중지합니다.")
        break # break : STOP.

number = 0
while number < 10:
    number = number + 1
    if number % 2 == 0: continue # continue : JUMP.
    print(number)