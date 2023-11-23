import mysql.connector

host='localhost'
username='root'
password='1995'
database = 'pet-adoption'

connect = mysql.connector.connect(host,username,password,database)
my_cursor=connect.cursor()

connect.commit()
connect.close()

print("Connection Successfully created !!")