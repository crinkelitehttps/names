#!/usr/bin/python
# put surnames into existing database

import psycopg2
import requests
from bs4 import BeautifulSoup

conn = psycopg2.connect("dbname=database user=joe")
cur = conn.cursor()

url = "http://names.mongabay.com/most_common_surnames.htm"
r = requests.get(url)
soup = BeautifulSoup(r.content,'lxml')
for rows in soup.find_all('tr')[1:]:
	try:
		for cells in rows.find_all('td')[0]:
			print(cells.capitalize())
	except:
		print("LIST ERROR!!!!")
