from bs4 import BeautifulSoup
import urllib2

f = open('C:\Python27\Projects\WebScrape\outputfileESPN.txt', 'w')

errorFile = open('C:\Python27\Projects\WebScrape\errorESPN.txt', 'w')

x = 0

while (x<10):
	soup = BeautifulSoup(
		urllib2.urlopen('http://www.polovniautomobili.com/putnicka-vozila/pretraga?page='+
			str(x) +'&brand=192&model=1824&showOldNew=all').read(), 'html')
	
	tableStats = soup.find("table", {"class" : "playerTableTable tableBody"})
	for row in tableStats.findAll('tr')[2:]:
		col = row.findAll('td')

		try:
			name = col[0].a.string.strip()
			f.write(name+'\n')

		except Exception as e:
			errorFile.write(str(x) + '********' + str(e) + '********' + str(col) + '\n')
			pass
	x = x +1
f.close
errorFile.close 