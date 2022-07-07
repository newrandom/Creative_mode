import mysql
import mysql.connector

# mysql 접속
mydb = mysql.connector.connect(host = '192.168.35.159', port = '3306', user=input('user:'), password=input('password:'))

mydb ; mycursor = mydb.cursor(buffered=True)

mycursor.execute('show databases')
mycursor.fetchall()


