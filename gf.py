import requests
from bs4 import BeautifulSoup
from func import extract_date

header = {
	'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
}

def get_articles(articles):
	for article in articles:
		title = article.h2.text
		arcticle_id = article['id']
		print(f'parsing post {arcticle_id} with title {title}')
		# if '|' in title:
		# 	date = title.split('|')[0].strip()
		# else:
		# 	date = title.split(' ')[0].strip()
		try:
			date = extract_date(title)
		except:
			date = 'unknown'
		link = article.find('h2',class_='entry-title taggedlink').a['href']
		article_dict[arcticle_id] = {
			'title' : title,
			'link' : link
		}
		url = link
		r = requests.get(url,headers=header).text
		soup = BeautifulSoup(r,'html.parser')
		paragraphs = soup.find_all('p')
		with open(f'./export_gf/{date}_{arcticle_id}.txt','w',encoding='utf8') as f:
			f.write(f'{title}\n')
			f.write(f'{link}\n')
			for p in paragraphs:
				# print(p.text)
				f.write(f'{p.text}\n')
			f.close()
article_dict = {}

url = 'http://www.traktor-boxhagen.de/category/spielberichte-der-grossfeldmannschaft'

r = requests.get(url,headers=header).text

soup = BeautifulSoup(r,'html.parser')

articles = soup.find_all('article')
nav = soup.find('div',class_='nav-previous').a['href']
get_articles(articles)


while nav is not None:
	r = requests.get(nav,headers=header).text
	soup = BeautifulSoup(r,'html.parser')
	articles = soup.find_all('article')
	try:
		nav = soup.find('div',class_='nav-previous').a['href']
	except AttributeError as e:
		nav = None
	get_articles(articles)