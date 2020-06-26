def add(a, b):
    return a + b
def sub(a, b):
    return a - b

if __name__ == "__main__": # 직접 모듈을 실행했을 경우 __name__이라는 변수에 __main__이 담겨져 수행 / import시에는 해당 묘듈의 이름이 변수에 담겨진다. ex) "_Module"
    print(add(1, 4))
    print(sub(1, 4))

# 클래스, 변수를 포함한 모듈
PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2)