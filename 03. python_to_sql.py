import mysql
import mysql.connector
import sys

# host 정보 확인
host = int(input('which is your host ? 1. local / 2. server     >> '))
if host == 1:
    host = '192.168.35.159'
elif host == 2:
    host = input('input server address: ')
else:
    sys.exit()

# mysql 접속
mydb = mysql.connector.connect(host = host, port = '3306', user=input('user : '), password=input('password : '))

mydb ; mycursor = mydb.cursor(buffered=True)

# use database
mycursor.execute('use lotto_db')

# DB에 저장된 최신 로또 회차 정보 조회
mycursor.execute('select ID from lotto_nums order by ID desc limit 1')
print(mycursor.fetchall()[0][0])        # >> 웹에 올라온 신규회차 정보와 비교하여 새로운 정보 입력해야 함.

mydb.close()        # 접속종료