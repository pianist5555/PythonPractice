# import pickle # 객체의 형태를 그대로 유지하면서 저장하고 불러오는 모듈
# f = open('pickleData.txt', 'wb')
# data = {1: 'python', 2: 'you need'}
# pickle.dump(data, f) # 세이브
# f.close()

# f = open('pickleData.txt', 'rb')
# data = pickle.load(f) # 로드
# print(data, type(data))
# f.close()

# import os # 운영체제 관련 모듈
# os.environ # 환경 변수에 대한 내용을 딕셔너리 객체로 돌려준다. => os.environ['PATH']
# os.chdir() # 디렉터리 위치를 변경할 수 있다.
# os.getcwd() # 현재 디렉터리 위치를 반환한다. 
# os.system('dir') # 시스템 명령어를 호출한다.
# f = os.popen('dir') # 호출한 시스템 명령어의 결괏값을 읽기 모드 형태의 파일 객체로 돌려준다.
# print(f.read())
# os.mkdir() # 디렉터리를 생성
# os.rmdir() # 디렉터리를 삭제 / 단 디렉터리가 비어있어야 가능
# os.unlink # 파일을 지운다.
# os.rename('src','dst') # src라는 파일을 dst라는 이름으로 변경

# import shutil # 파일을 복사하는 모듈
# shutil.copy('src.txt', 'dst.txt') # 파일을 복사한다.

# import glob # 디렉터리 안의 파일들을 리스트로 읽어들이는 모듈
# print(glob.glob('C:/검열/검열/검열/GitHub/PythonPractice/*')) #  해당위치에 있는 파일을 모두 찾아서 읽어 들인다. / 메타 문자 사용 가능 ex) *, ? 등

# import tempfile # 임시 저장공간으로 사용할 파일 객체를 돌려주는 모듈
# filename = tempfile.mkstemp()
# f = tempfile.TemporaryFile()
# f.close()

# import time # 시간과 관련된 모듈
# time.time() # UTC(1970/01/01/00.00.00)를 기준으로 지난 시간을 초단위로 반환해준다.
# time.localtime(time.time()) # time.time()이 돌려준 실수 값을 변환하여 사람이 읽기 쉽게 반환해준다.
# time.asctime(time.localtime(time.time())) # 튜플 형식으로 인수를 받아서 받아서 더 알아보기 쉽게 문자열로 반환해준다. 
# time.ctime() # ... 를 편하게 코딩할 수 있다... == time.asctime(time.localtime(time.time()))
# time.strftime('&d', time.localtime(time.time())) # 포맷 코드를 사용해 시간 출력
# time.sleep(1) # 1초 동안 대기한다. 반복문에 자주 사용되고 일정한 시간 간격으로 루프를 실행할 수 있다.

# import calendar # 달력을 볼 수 있게 해주는 모듈
# calendar.calendar(2020) # = calendar.prcal(2015) / 해당 년도의 달력을 출력한다.
# calendar.weekday(2020, 6, 26) # 월요일 ~ 일요일에 맞는 숫자(0~6)를 돌려준다.
# calendar.monthrange(2020, 12) # 달의 1일의 요일을 숫자로 돌려주고 며칠까지 있는지를 튜플 형식으로 돌려준다.

import random # 난수 관련 모듈
random.random() # 0.0 ~ 1.0 사이의 실수 중 난수 값을 돌려준다.
random.randint(1,100) # 1 ~ 100 사이의 정수 중 난수 값을 돌려준다.

data = [1,2,3,4,5]
def random_pop_two(data):
    number = random.choice(data) # 넘겨 받은 리스트에서 무작위로 한개를 선택해 반환한다.
    data.remove(number)
    return print(number)
random_pop_two(data)

random.shuffle(data) # 리스트의 요소들을 랜덤으로 섞는다.

import webbrowser # 웹 브라우저 모듈
webbrowser.open("http://google.com") # 자신의 시스템의 기본 브라우저를 이용해 해당 사이트로 이동한다.