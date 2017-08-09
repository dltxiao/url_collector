import mysql.connector

def sqlwrite(url):
    top = url.split('.')[-1]
    second = url.split('.')[-2]
    try:
        third = url.split('.')[-3]
    except:
		third = ''
    conn = mysql.connector.connect(user='zhong', password='xiao', database='url_collector')
    cursor = conn.cursor()
    #cursor.execute('create table url2 (url char(128) primary key)')
    try:
        cursor.execute('insert into urls (domain, top, second, third, sub_class_id) value (%s, %s, %s, %s, %s)', [url, top, second, third, 120])
        conn.commit()
    except:
        pass
    cursor.close()

if __name__ == '__main__':
    sqlwrite('test2.com')
