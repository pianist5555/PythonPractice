import time
import threading # 스레드 모듈

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s" % i)
print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task) # 스레드 생성
    threads.append(t)
for t in threads:
    t.start() # 스레드 실행
for t in threads:
    t.join() # 스레드가 종료될 때까지 기다리게 한다.

print("End")