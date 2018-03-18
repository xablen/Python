import os;
import csv;
import requests;
import re;
from bs4 import BeautifulSoup;

for numb in ('0', '5'):
	expression = ('url' + numb + '.htm')
	requete = requests.get(expression)
	page = requete.content
	soup = BeautifulSoup(page, 'html.parser')
		
	b = soup.find_all("b", {"class": "s2"})
	for p in b:
		print(p.text)
