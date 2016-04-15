#!/usr/bin/python
#scrape names to database
import psycopg2
from bs4 import BeautifulSoup

conn = psycopg2.connect("dbname=database user=postgres")
cur = conn.cursor()

f = open('/home/joe/git/python/names/names.html', 'r')
data = f.read()
soup = BeautifulSoup(data, 'lxml')
soup = BeautifulSoup(str(soup.find_all('table')[1]))
soup = BeautifulSoup(str(soup.find_all('tr')[2:-2]))
for id, tr in enumerate(soup.find_all('tr')):
	rank, boy, girl = tr.find_all('td')
	cur.execute("INSERT INTO test (rank, boy, girl, id) VALUES (%s, %s, %s, %s)",
		(rank.text, boy.text, girl.text, id))
conn.commit()
cur.close()
conn.close()
