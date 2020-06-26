money = True
card = 3000
if money and card >=2000: # and or not
    print("택시를 타고 가라")
else:
    print("걸어 가라")

if money or card >=5000:
    print("아이스크림을 카드로 사먹어라")
else:
    print("아이스크림은 먹지 마라")

if not money!=False:
    print("돈이 없다")
else:
    print("돈이 있다")

if 1 in [1,2,3]: # not in : 리스트 튜플 문자열
    print("[1, 2, 3] 안에 1이 들어있다.")

if 1 not in [2,3,4]:
    print("[2, 3, 4] 안에 1은 없다.")

pocket = ["paper","money","card"]
if 'money' in pocket:
    print("돈을 꺼내라.")
    pass # pass : Do not anything.
elif 'paper' in pocket:
    print("paper를 꺼내라.")
else:
    print("카드를 꺼내라.")