import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='krakra', db='fyp_cbrs')
cur = conn.cursor()
query = 'select description from description'
cur.execute(query)
fetched_rows = cur.fetchall()
descriptions_list = []
for row in fetched_rows:
    descriptions_list.append(row[0])
print(descriptions_list[8])
cur.close()
conn.close()