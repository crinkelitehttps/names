#!/usr/bin/python

#scrape names to database

from bs4 import BeautifulSoup

f = open('names.html', 'r')
data = f.read()
soup = BeautifulSoup(data, 'lxml')
num = 1
for i in soup.find_all('tr'):
	print(soup.find_all('td')[num])
	num+=3


