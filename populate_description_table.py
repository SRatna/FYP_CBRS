import pymysql
from mimesis import Text
data = Text('en')

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='krakra', db='fyp_cbrs')
cur = conn.cursor()
query = 'insert into description values (%s, %s)'
for i in range(1,101):
    cur.execute(query, (i, data.text(10)))
conn.commit()
cur.close()
conn.close()