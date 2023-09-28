#2컴퓨터의 외부 및 내부 ip확인하기
#import socket 
# from requests import get
# import re

# in_add = socket.gethostbyname(socket.gethostname()) #내부 ip
# print(in_add)

# in_add = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
# in_add.connect(("www.google.co.kr", 443))
# print(in_add.getsockname()[0])

# print("Host Name ",socket.gethostname())
 
# print("IP Address(Internal) : ",socket.gethostbyname(socket.gethostname()))
 
# print("IP Address(External) : ",socket.gethostbyname(socket.getfqdn()))

# #3 음성출력 
# from gtts import gTTS


# text = "안녕하세요" 

# tts = gTTS(text=text , lang="ko")
# filename = "c:/Users/user/Desktop/1단계 스터디/" + "text.mp3" 
# tts.save(filename)
# # playsound(r'/content/3. 텍스트를 음성으로 변환\hi.mp3')

#6
# import itertools
# import zipfile
# def un_zip(password_string , min_len , max_len , zFile):
#     for len in range(min_len,max_len+1):
#         to_attempt = itertools.product(password_string,repeat= len)
#         for attempt in to_attempt:
#             password = ''.join(attempt)
#             print(password)
#             try:
#                 zFile.extractall(pwd = password.encode())
#                 print(f"비밀번호는 {password}입니다.")
#                 return 1
#             except:
#                 pass
        

# password_string = '0123456789abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ'

# zFile = zipfile.ZipFile(r'C:/Users/user/Desktop/1단계 스터디/암호1234.zip')

# min_len = 1
# max_len = 5

# un_zip_result = un_zip(password_string , min_len , max_len , zFile)

# if un_zip_result ==1:
#     print("암호찾기 성공")
# else:
#     print("암호찾기 실패")


# #7 환율 변환기
# from currency_converter import CurrencyConverter
# from bs4 import BeautifulSoup
# import requests
# # cc= CurrencyConverter()
# # print(cc.currencies) #통화 목록 출력
# cc= CurrencyConverter()
# print(cc.convert(1, 'USD' , 'EUR'))

# def get_exchange_rate(target1 , target2):
#     headers = {
#         "User-Agent" : "Mozilla/5.0",
#         "Content-Type" : "text/html; charset=utf-8"
#     }
#     response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1 , target2), headers=headers)
#     content = BeautifulSoup(response.content , 'html.parser')
#     contains = content.select("#__next > div.desktop\:relative.desktop\:bg-background-default > div > div > div.grid.gap-4.tablet\:gap-6.grid-cols-4.tablet\:grid-cols-8.desktop\:grid-cols-12.grid-container--fixed-desktop.general-layout_main__LHpKS > main > div > div.instrument-header_instrument-header__i63mN.mb-5.bg-background-surface.tablet\:grid.tablet\:grid-cols-2 > div:nth-child(2) > div.instrument-price_instrument-price__2w9MW.flex.items-end.flex-wrap.font-bold > span")
#     print(contains[0].get_text())



# get_exchange_rate("usd" , "krw")

#8 쓰레드를 사용한 프로그램
# import threading
# import time 

# def thread_1():
#     while True:
#         print("쓰레드 1 동작")
#         time.sleep(1.0)

    
# t1 = threading.Thread(target=thread_1)
# t1.daemon = True
# t1.start()

# while True: 
#     print("메인동작")
#     time.sleep(2.0)

#멀티 쓰레드
# def sum(name,value):
#     for i in range(0,value):
#         print(f"{name}:{i}")

# t1 = threading.Thread(target=sum , args=("1번 쓰레드" , 10 ))
# t2 = threading.Thread(target=sum , args=("2번 쓰레드", 10))

# t1.start()
# t2.start()

# print("메인 쓰레드\n")

#자동화 프로그램 만들기.

from bs4 import BeautifulSoup
import googletrans
import requests
import json


url = 'https://www.gutenberg.org/cache/epub/84/pg84.txt'
html = requests.get(url)
soup = BeautifulSoup(html.text , 'html.parser')
# script_tag = content.find_all(['script', 'style', 'header', 'footer', 'form'])
# #태그 제거
# for script in script_tag:
#     script.extract()

content = soup.get_text('\n ' , strip=True) #strip=True는 공백제거 및 개행제거

content1 = list(content)
content2 = content1.split(maxsplit=5000)
print(content2)



# transltor = googletrans.Translator()
# result = transltor.translate(content1, dest = "ko")
# print(result.text)
