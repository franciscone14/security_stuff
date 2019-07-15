import requests
from bs4 import BeautifulSoup

host = "http://10.10.11.8/dvwa/login.php"

login_page = requests.get(host)

content = BeautifulSoup(login_page.content, features="html.parser")

user_token = content.find(type="hidden").get('value')

data = {
	'username': 'admin',
	'password': 'password',
	'Login': 'Login',
	'user_token': user_token
}

headers = {
	'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
	'content-type': 'application/x-www-form-urlencoded',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'accept-encoding': 'gzip, deflate',
	
}

cookies = {
	'security': login_page.cookies['security'],
	'PHPSESSID': login_page.cookies['PHPSESSID']
}

r = requests.post(host, headers=headers, cookies=cookies, data=data)

print(BeautifulSoup(r.content, features="html.parser").prettify())
