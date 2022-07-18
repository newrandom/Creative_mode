# 로또번호 조회 프로그램

## `feature`
> - 특정 숫자를 제외한 난수 6개 생성 가능 (선택)
> - 최근 10번, 25번, 50번, 전체 당첨번호 중 가장 많이 나온 숫자 안내 (기능 준비 중)
> - 시작회차, 종료회차를 선택하여 조회하여 가장 많이 나온 당처번호 안내 (기능 준비 중)

## `현재 진행상황`
> - tkinter 모듈을 활용
> - selenium 의 webdriver를 이용하여 동행복권(`https://dhlottery.co.kr/gameResult.do?method=byWin`)의 당첨정보 스크래핑
> - pandas를 이용하여 데이터 편집, local에 저장 (추후 SQL에 바로 업로드 하는 과정으로 변경할 것)
> - NAS의 SQL에 데이터 업로드 

## `추후 예정상황`
> - SQL의 데이터 불러온 후, tkinter 설정에 바로 연동
> - ~~selenium은 webdriver (Chromedriver)의 활용이 필요한데, 다른 방법으로 스크래핑 할 수 있는지 찾아보기 (ex. BeautifulSoup)~~ \
> - 실행파일로 만들기
> - tkinter 내의 함수, 알고리즘 정리하기


## `pip list`
> - `from tkinter import *`
> - `from random import sample`
> - `from tkinter.ttk import Combobox`
> 
> - `import mysql`
> - `import mysql.connector`
>
> - `import requests`
> - `from bs4 import BeautifulSoup`
> - `from selenium import webdriver`
> - `from selenium.webdriver.common.keys import Keys`
> - `from selenium.webdriver.common.by import By`
> - `from selenium.webdriver.support.select import Select`
> - `import pandas as pd`
