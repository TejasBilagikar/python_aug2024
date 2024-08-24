import pymysql  

try:
    connectionObj = pymysql.Connect(host='localhost', port=3306, user='root', password='root123', database='tejas_db', charset='utf8')
    print('Database connected succesfully.')
    connectionObj.close()
except:
    print('Database connection failed.')