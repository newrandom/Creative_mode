# 로또번호 조회 프로그램

## `feature`
> - 특정 숫자를 제외한 난수 6개 생성 가능 (선택사항)
> - 최근 10번, 25번, 50번, 전체 당첨번호 중 가장 많이 나온 숫자 안내 (기능 준비 중)
> - 시작회차, 종료회차를 선택하여 조회하여 가장 많이 나온 당첨번호 안내 (기능 준비 중)
> - 누적 데이터를 활용하여 다음 로또번호 예측하기 (추후)

## `현재 진행상황`
> - tkinter 모듈을 활용
> - ~~selenium 의 webdriver를 이용하여 동행복권(`https://dhlottery.co.kr/gameResult.do?method=byWin`)의 당첨정보 스크래핑 (완료)~~
> - ~~pandas를 이용하여 데이터 편집, local에 csv로 저장 (추후 SQL에 바로 업로드 하는 과정으로 변경할 것) (완료)~~
> - ~~NAS의 SQL에 데이터 업로드 (완료)~~

## `추후 예정상황`
> - SQL의 데이터 불러온 후, tkinter 설정에 바로 연동
> - ~~selenium은 webdriver (Chromedriver)의 활용이 필요한데, 다른 방법으로 스크래핑 할 수 있는지 찾아보기 (ex. BeautifulSoup)~~
> - 실행파일로 만들기
> - tkinter 내의 함수, 알고리즘 정리하기
> - SQL 데이터를 불러와 딥러닝 예측하기
> - 사용설명서 작성하기
> - SQL 접속 유저 및 접속 권한 

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
> - `from selenium.webdriver.support.ui import Select`
> - `import pandas as pd`
> - `import sys, time`


## `Feedback`
> - 홈페이지에서 회차 조회를 for 문을 이용하여 반복해서 조회할 때, `driver.find_element(By.XPATH, '//*[@id="dwrNoList"]').send_keys(i)` 를 사용하였는데, 해당 element가 str 타입이어서, send_keys가 제대로 작동하지 않았음.
> - 이에 `from selenium.webdriver.support.ui import Select`의 `select_by_value(str(i))`를 이용하여 value를 차례대로 선택할 수 있었고, 데이터가 올바르게 들어가는 것을 확인하였음.
