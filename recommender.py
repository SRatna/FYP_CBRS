import pymysql
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='krakra', db='fyp_cbrs')
cur = conn.cursor()
query = 'select description from description'
cur.execute(query)
fetched_rows = cur.fetchall()
descriptions_list = []
for row in fetched_rows:
    descriptions_list.append(row[0])

tfidf = TfidfVectorizer().fit_transform(descriptions_list)

insert_query = 'insert into similar_products values (%s, %s)'
for i in range(0, 100):
    cosine_similarities = linear_kernel(tfidf[i:i+1], tfidf).flatten()
    related_products_indices = cosine_similarities.argsort()[:-7:-1]
    for j in related_products_indices:
        if i != j:
            cur.execute(insert_query, (str(i+1), str(j+1)))
conn.commit()
cur.close()
conn.close()