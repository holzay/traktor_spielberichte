from datetime import datetime

def extract_date(date_str,orig_paragraph):
	if '|' in date_str:
		date_str = date_str.split('|')[0].strip()
	else:
		date_str = date_str.split(' ')[0].strip()
	date_str = date_str.replace('`','')
	vday = date_str.split('.')[0].zfill(2)
	vmonth = date_str.split('.')[1].zfill(2)
	vyear = date_str.split('.')[2]
	if len(vyear)==2:
		vdate = datetime.strptime(f'{vday}.{vmonth}.{vyear}', '%d.%m.%y')
	else:
		vdate = datetime.strptime(f'{vday}.{vmonth}.{vyear}', '%d.%m.%Y')
	return vdate.strftime('%Y-%m-%d')

def traktor_clean_article(text):
	if '\n' in text and text.split('\n')[1][:1].isnumeric():
		return text.split('\n')[1]
	elif '\n' in text and text.split('\n')[0][:1].isnumeric():
		return text.split('\n')[0]
	else:
		return text