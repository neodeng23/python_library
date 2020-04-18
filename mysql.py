import MySQLdb

conn = MySQLdb.connect(
    host = '192.168.1.1',
    user='xxxx',
    passwd = 'xxxx',
    db = 'plesson',
    charset = 'utf8',
)

c = conn.cursor()  #建立游标
c.execute('select * from sq_data')
row = c.fetchone()  #返回一行结果

#fetchall()一次性直接读出所有
rows = c.fetchall()         #数据量过大时，容易崩溃
print(rows)

#用循环读出所有
for i in range(c.fowcount):
    row = c.fetchone
    if row[1] == 'python':
        print('find')
        break

#插入数据
c.execute('INSERT INTO sq_course(NAME,'desc',display_idx) VALUES('xx' ,'xxx','6')')
conn.commit()