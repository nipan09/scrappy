from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse

def nav_view(request):
	url = 'https://www.moneycontrol.com/mutual-funds'
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find_all('a', class_='robo_medium')
	detail = []
	for elem in results:
		detail.append({"text": elem.text, "href": elem.attrs['href']})
	url = []
	for fund in range(len(detail)):
		if "Axis Bluechip Fund - D (G)" in detail[fund].values():
			url.append(detail[fund].get("href"))
	page1 = requests.get(url[0])
	soup1 = BeautifulSoup(page1.content, 'html.parser')
	results1 = soup1.find('div', class_='leftblok')
	print(results1)
	abcd = results1.find('span', class_='amt')
	amt = abcd.text
	return HttpResponse(amt)

