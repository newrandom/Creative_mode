import mysql
import mysql.connector
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import sys, time

# ====================== #

# host 정보 확인
host = int(input('which is your host? 1. local / 2. server  >> '))
if host == 1:
    host = '192.168.35.159'
elif host == 2:
    host = input('input server address: ')
else:
    sys.exit()
    
mydb = mysql.connector.connect(host = host, port = '3306', user=input('user name : '), password = input('password : '))
mydb

table_name = 'lot_num'      # table name 지정

mycursor = mydb.cursor(buffered = True)


## =========== USE DB ============= ##
mycursor.execute('USE lotto_db')

## =========== Table ======== ##

# DB 에 새로운 TABLE 만들기
mycursor.execute('SHOW TABLES')
find_table = mycursor.fetchall()

if ('{}'.format(table_name),) in find_table:     # TABLE 중복 여부 확인
    print("{} 이라는 테이블이 이미 DB에 존재합니다.".format(table_name))

else:       # TABLE 이 없을 때, 새로 만들기
    mycursor.execute('CREATE TABLE {} (ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, NUM1 INT NOT NULL, NUM2 INT NOT NULL, NUM3 INT NOT NULL, NUM4 INT NOT NULL, NUM5 INT NOT NULL, NUM6 INT NOT NULL)'.format(table_name))
    mydb.commit()
    print('{} 이라는 테이블을 새로 만들었습니다.'.format(table_name))

# TABLE 의 DESC 확인
# mycursor.execute('DESC {}'.format(table_name))
# print(mycursor.fetchall())

# DB에 저장된 모든 회차 정보 조회
mycursor.execute('SELECT ID FROM {} ORDER BY ID DESC'.format(table_name))
all_num_in_sql = mycursor.fetchall()
all_num_in_sql = [all_num_in_sql[i][0] for i in range(0,len(all_num_in_sql))]
# print(all_num_in_sql)       # 저장된 전체 회차 조회

# # DB에 저장된 최신 회차 정보 조회
# mycursor.execute('SELECT * FROM {} ORDER BY ID DESC LIMIT 1'.format(table_name))
# latest_num_in_sql = mycursor.fetchall()
# print(latest_num_in_sql[0])
# print(f'TABLE에 저장된 최신회차는 : {latest_num_in_sql} 회차 입니다.')

## ========= Page access ======= ##

# 로또 홈페이지 접속
service = Service('./chromedriver')
url = 'https://www.dhlottery.co.kr/gameResult.do?method=byWin'
try:
    driver = webdriver.Chrome(service = service)
except:
    print('chromedriver의 버전을 확인해 주세요 😣')
    time.sleep(2)
    sys.exit()

driver.get(url)

# 최신회차 조회
new = int(driver.find_element(By.XPATH, '//*[@id="dwrNoList"]').text.strip().split()[0])
print('최신 회차 : {}회'.format(new))

# 최신회차 검사
if new in all_num_in_sql:
    print('최신 회차 ({})가 DB에 저장되어 있습니다.'.format(new))
    mycursor.execute('SELECT * FROM {} ORDER BY ID DESC LIMIT 1'.format(table_name))
    latest_nums = list(mycursor.fetchall()[0])
    print('({}회차 : {})'.format(latest_nums[0], latest_nums[1:]))

elif all_num_in_sql == []:
    print('TABLE 에 로또 정보가 없습니다.')
    q = int(input('웹에서 정보를 받아오시겠습니까? (1 : yes, 2: no) '))
    if q == 1:

        for i in range(1, new+1):     # 1회차 부터 신규 회차까지 루프 > 데이터 저장

            select = Select(driver.find_element(By.XPATH, '//*[@id="dwrNoList"]'))      # 드롭박스 선택
            select.select_by_value(str(i))       # value 선택

            # driver.find_element(By.XPATH, '//*[@id="dwrNoList"]').send_keys(i)        ### >> 삭제 // 해당 element의 값이 str 형식으로, i키를 받으면 오류가 발생
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH, '//*[@id="searchBtn"]').send_keys(Keys.ENTER)     # 조회버튼 클릭

            nums = []
            for _ in range(1, 7):

                # 신규 회차의 로또번호 6개를 리스트에 넣기
                nums.append(driver.find_element(By.XPATH, '//*[@id="article"]/div[2]/div/div[2]/div/div[1]/p/span[{}]'.format(_)).text)

            # 새로운 회차 및 번호 DB에 저장
            print({i}, '회차가 저장됩니다.', '{}'.format(nums))
            mycursor.execute('INSERT INTO {} (ID, NUM1, NUM2, NUM3, NUM4, NUM5, NUM6) VALUES ({}, {}, {}, {}, {}, {}, {})'.format(table_name, i, nums[0],nums[1],nums[2],nums[3],nums[4],nums[5]))
                                            ## {table_name} table desc : ID, num1 ~ num6
            mydb.commit()       # 커서의 쿼리 실행 저장

            # DB의 저장된 데이터 확인
            mycursor.execute('SELECT * FROM {} ORDER BY ID DESC LIMIT 1'.format(table_name))
            latest_info = mycursor.fetchall()[0]
            print('{} 회차 : [{}, {}, {}, {}, {}, {}] 저장 됨'.format(latest_info[0], latest_info[1],latest_info[2],latest_info[3],latest_info[4],latest_info[5],latest_info[6]))
            
else:
    print('최신 회차 ({})가 저장되어 있지 않습니다. (현재 저장되어있는 최신회차 : {}회)'.format(new, all_num_in_sql[0]))
    q = int(input('최신회차 정보를 업데이트 하시겠습니까? (1 : yes, 2: no)'))
    if q == 1:

        for i in range(all_num_in_sql[0]+1, new+1):     # DB에 저장된 최신회차 + 1 부터 신규 회차까지 루프 > 데이터 저장
            
            select = Select(driver.find_element(By.XPATH, '//*[@id="dwrNoList"]'))      # 드롭박스 선택
            select.select_by_value(str(i))       # value 선택   

            # driver.find_element(By.XPATH, '//*[@id="dwrNoList"]').send_keys(i)        ### >> 삭제 // 해당 element의 값이 str 형식으로, i키를 받으면 오류가 발생
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH, '//*[@id="searchBtn"]').send_keys(Keys.ENTER)     # 조회버튼 클릭

            nums = []
            for _ in range(1, 7):

                # 신규 회차의 로또번호 6개를 리스트에 넣기
                nums.append(driver.find_element(By.XPATH, '//*[@id="article"]/div[2]/div/div[2]/div/div[1]/p/span[{}]'.format(_)).text)

            # 새로운 회차 및 번호 DB에 저장
            print({i}, '회차가 저장됩니다.', '{}'.format(nums))
            mycursor.execute('INSERT INTO {} (ID, NUM1, NUM2, NUM3, NUM4, NUM5, NUM6) VALUES ({}, {}, {}, {}, {}, {}, {})'.format(table_name, i, nums[0],nums[1],nums[2],nums[3],nums[4],nums[5]))
                                            ## {table_name} table desc : ID, num1 ~ num6
            mydb.commit()       # 커서의 쿼리 실행 저장

            # DB의 저장된 데이터 확인
            mycursor.execute('SELECT * FROM {} ORDER BY ID DESC LIMIT 1'.format(table_name))
            latest_info = mycursor.fetchall()[0]
            print('{} 회차 : [{}, {}, {}, {}, {}, {}] 저장 됨'.format(latest_info[0], latest_info[1],latest_info[2],latest_info[3],latest_info[4],latest_info[5],latest_info[6]))
            
driver.close()
mydb.close()
