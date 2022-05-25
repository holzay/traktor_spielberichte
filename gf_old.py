import requests
from bs4 import BeautifulSoup
from func import extract_date,traktor_clean_article
import os

header = {
	'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0'
}


chapter_dict = {

'Fz-Verbandsliga | Saison 2016/17' : '2016-2017_FZ_Verbandsliga',
'Fz-Verbandsliga | Saison 2015/16' : '2015-2016_FZ_Verbandsliga',
'Landesliga I | Saison 2014/15' : '2014-2015_Landesliga_I',
'Bezirksliga II | Saison 2013/2014' : '2013-2015_Bezirksliga_II',
'Kreisliga A | Saison 2012/2013' : '2012-2013_Kreisliga_A'
}

os.chdir(r'D:\Code\traktor_spielberichte\export_gf_old')


url = 'http://s600778792.online.de/grossfeld_saisons'

r = requests.get(url,headers=header).text

soup = BeautifulSoup(r,'html.parser')

with open('output.html','w',encoding='utf8') as log:
	log.write(soup.prettify())

articles = soup.find_all('div',class_='sp-wrap sp-wrap-default')

article_id = 0
arcticle_dict = {}

for article in articles:
	chapter = article.find('div',class_='sp-head unfolded') or article.div.text
	chapter = chapter.replace('\n','').strip()
	if chapter == 'Kreisliga A | Saison 2012/2013':
		print('debug!')
	folder_name = chapter_dict[chapter]
	if not os.path.isdir(f'./{folder_name}'):
		os.mkdir(folder_name)
	paragraphs = article.find_all('p')
	file_open = False
	for p in paragraphs:
		# try:
		# 	title = p.strong.text.strip()
		# except:
		# 	title = None
		# if title:
		strong_tag = p.find('strong')
		multiple_strong_tags = p.find_all('strong')
		if strong_tag:
			# for strong_tag in strong_tags:
			if file_open:
				f.close()
				file_open = False
			title = strong_tag.text.strip()
			if not title[:1].isnumeric():
				continue
			article_id+=1
			article_text = []
			try:
				date = extract_date(title,title)
			except:
				print(f'problem with {title}')
			if len(multiple_strong_tags)>1:
				for index,s_tag in enumerate(multiple_strong_tags):
					if index == 0:
						pass
					else:
						title = f'{title}\n{s_tag.text.strip()}'
			f = open(f'../export_gf_old/{folder_name}/{date}_{article_id}.txt','w',encoding='utf8')
			# f.write(f'{title}\n')
			file_open = True
			# texts = p.find_next_siblings('p')
		if file_open:
			f.write(f'{p.text.strip()}\n')
			


			# with open(f'./export_gf_old/{date}_{article_id}.txt','w',encoding='utf8') as f:
			# 	for text in texts:
			# 		for child in text.children:
			# 			if child.name == 'strong' or child.contents[0].name == 'strong':
			# 				break
			# 		f.write(text.text)
					# if text.contents[0].name:
					# 	if text.contents[0].name == 'strong' or text.contents[1].name == 'strong':
					# 		break
					# else:
						# f.write(text.text)

				
			





		# text = p.text
		# try:
		# 	title = p.strong.text
		# 	title = traktor_clean_article(title)
		# 	try:
		# 		f.close()
		# 	except NameError:
		# 		pass
		# 	first_paragraph = True
			
		# except AttributeError as e:
		# 	title = None
		# 	first_paragraph = False
		# if first_paragraph:
		# 	text = traktor_clean_article(text)
		# 	# date = text.split('|')[0].strip()
		# 	try:
				
			
		# 	article_id+=1
		# 	f = open(f'./export_gf_old/{date}_{article_id}.txt','w',encoding='utf8')
		# 	f.write(f'{text}\n')
		# elif title is None:
		# 	try:
		# 		f.write(f'{text}\n')
		# 	except NameError:
		# 		pass
			
