import httplib2
import json
from datetime import datetime
import os

city = input("enter city name that you live in : ") # 자신의 도시 입력받을 변수
url = 'http://api.openweathermap.org/data/2.5/weather?units=Metric&q=' #open api 웹페이지 주소
mykey= '&APPID=f6e048b59f4c0712991a69112caf67a3' # open api 사용위해서 받은 키

http=httplib2.Http()
# http 캐시 활성화(?)
myrequest = url+city+mykey
# url에 살고 있는 도시와 key를 더해서 최종 url을 만든다
response, content = http.request(myrequest, 'GET')
# 서버의 응답(헤더)과 내용(사전 같은 객체(dictionary-like object)) 받아옴
result = json.loads(content.decode('utf-8'))
# 받아온 내용을 딕셔너리로 변환

# humidity, temperature, weather 받아오기

humidity = result['main']['humidity']
# main 이라는 key에 해당하는 값이 딕셔너리로 되어있고 그 중 humidity 키가 있고 값으로 습도가 넣어져있다.
temp = result['main']['temp']
# 마찬가지로 main 키에 해당하는 값인 딕셔너리에 temp 키가 있고 그 값으로 온도가 넣어져 있다.
weather = result['weather'][0]['main']
# weather 키에 해당하는 값이 리스트로 되어있고, 리스트 인덱스 0번에 딕셔너리가 들어있고
# main 키에 해당하는 값으로 날씨 상태가 넣어져 있다.

now=datetime.now() # 현재 시간을 받아오기 위한 datetime 함수
# 각각 년,월,일 시,분,초 를 받아옴
year=now.year
month=now.month
day=now.day
hour=now.hour
minute=now.minute
sec=now.second
print("current date and time is %s-%s-%s %s:%s:%s"%(year, month, day, hour, minute, sec))
print(city+''' 's weather is '''+weather)
print('current temperature : %d'%temp)
print('current humidity : %d'%humidity)

def discomfort_index(temp, humidity): # 불쾌지수 구하기 위한 함수
    DI=(9/5)*temp-0.55*(1-(humidity/100))*((9/5)*temp-26)+32 # 불쾌지수 구하는 공식
    return DI

dis_index = discomfort_index(temp,humidity) # 불쾌지수
print('discomfort index is %.2f'%dis_index)

def solution() : # 불쾌지수를 줄일 수 있는 해결책을 출력해주는 함수
    print("\n")
    select = input("불쾌지수를 줄일 해결책을 보겠습니까? yes or no ")
    print("\n\n\n\n")
    if select == 'yes' :
        dir = os.path.dirname(os.path.realpath(__file__)) # 파일이 있는 현재 디렉토리의 경로 가져옴
        f_dir = dir+"/solution.txt" # 디렉토리 경로에 파일명을 붙여 최종 경로를 만듬
        # 파일이 없을 경우에 대비한 예외처리
        try :
            file = open(f_dir,'r')  # 해결책을 써놓은 파일을 불러옴
            output = file.read() # 파일 전체 내용을 문자열로 리턴
            print(output) # 출력
            file.close()
        except FileNotFoundError as e : # 파일이 없을 경우 이 곳으로 넘어온다.
            print("파일이 없습니다.")
    else :
       print("- END -")

print("\n")
# 불쾌지수에 따른 불쾌의 정도
if dis_index >= 80 :
    print(" 모든 사람들이 불쾌감을 느낄 수 있는 불쾌 지수에요!!!!!! ")
    solution()
elif dis_index >= 75 and dis_index < 80 :
    print(" 50% 정도의 사람들이 불쾌감을 느낄 수 있는 정도에요!")
    solution()
elif dis_index >=68 and dis_index < 75 :
    print(" 불쾌감을 느끼기 시작하는 정도에요, 아직은 괜찮아요!")
    solution()
elif dis_index > 0 and dis_index < 68 :
    print("쾌적함을 느낄 수 있어요!! 오늘 하루는 쾌적하게!!")
    solution()
