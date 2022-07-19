# import module
import pandas as pd
from selenium import * 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import sys, time

# read_csv
dataframe = pd.read_csv('./result/lotto_result.csv', index_col = 0)
latest_result = int(dataframe.iloc[-1].name)
print('저장되어 있는 최신 회차 : {}회'.format(latest_result))

# 로또 홈페이지 최신 회차 조회_1 : 홈페이지 접속

service = Service('./chromedriver')        # == 추가 == # webdriver 의 service 활용     
url = 'https://www.dhlottery.co.kr/gameResult.do?method=byWin'

try :       # chromedriver 의 버전이슈 등의 문제가 발생하지 않을 때 계속 진행
    driver = webdriver.Chrome(service=service)  # 크롬드라이버 서비스 받아오기

except:     # chromedriver 의 버전이슈 등의 문제가 발생 시, 프로그램 종료
    print('chromedriver의 버전을 확인해 주세요 😣')
    time.sleep(2)
    sys.exit()

driver.get(url)

# 로또 홈페이지 최신 회차 조회_2 : 최신회차조회
new = int(driver.find_element(By.XPATH, '//*[@id="dwrNoList"]').text.strip().split()[0])
print('최신 회차 : {}회'.format(new))

# 최신회차 검사
if new in dataframe.index:
    print('최신 회차 ({})가 저장되어 있습니다.'.format(new))

else:
    print('최신 회차 ({})가 저장되어 있지 않습니다. (현재 저장되어있는 최신회차 : {}회)'.format(new, latest_result))
    q = int(input('최신회차 정보를 업데이트 하시겠습니까? (1 : yes, 2: no)'))
    if q == 1:
        
        for i in range(latest_result+1, new+1):     # 저장된 최신회차+1 부터 신규 회차까지루프 > 데이터 저장
            
            driver.find_element(By.XPATH, '//*[@id="dwrNoList"]').send_keys(i)
            driver.implicitly_wait(10)
            driver.find_element(By.XPATH, '//*[@id="searchBtn"]').send_keys(Keys.ENTER)

            nums = []
            for _ in range(1, 7):
                
                # 신규 회차의 로또번호 6개
                nums.append(driver.find_element(By.XPATH, '//*[@id="article"]/div[2]/div/div[2]/div/div[1]/p/span[{}]'.format(_)).text)

            print({i}, '회차가 저장됩니다.' , '{}'.format(nums))
            dataframe.loc[dataframe.iloc[-1].name + 1] = nums
        
        dataframe.to_csv('./result/lotto_result.csv')      # 최신 정보 저장

driver.close()