from bs4 import BeautifulSoup
from sklearn import linear_model
import urllib2

f = open('C:\Python27\Projects\WebScrape\outputfilePOLOVNI.txt', 'w')
p = open('C:\Python27\Projects\WebScrape\outputfilePOLOVNIcena.txt', 'w')

errorFile = open('C:\Python27\Projects\WebScrape\errorESPN.txt', 'w')
x = 0

while (x<45):
	soup = BeautifulSoup(
		urllib2.urlopen('http://www.polovniautomobili.com/putnicka-vozila/pretraga?page='+
			str(x) +'&brand=192&model=1824&showOldNew=all').read(), 'html.parser')
	
	wholeList = soup.find("ul", {"id" : "searchlist-items"})

	for listItem in wholeList.findAll('li'):
		#pronalazi deo sa kilometrazom, godistem i cenom
		additional = listItem.findAll("div", {"class" : "title-additional"})

		if(additional!=[]):
			divAdditional = additional[0]

			itemsAdditional = divAdditional.findAll("div")
			
			km = itemsAdditional[0].string.strip()[:-3]

			km = km.replace(".", "")

			year = itemsAdditional[1].string.strip()[:-5]
			
			price = itemsAdditional[2].string.strip()[:-1].strip()
			price = price.replace(".", "")


			infoBox = str(listItem.findAll("div", {"class" : "ad-infobox"})[0])
			
			soupica = BeautifulSoup(infoBox, 'html.parser')
			allInfo = soupica.get_text()
			infoArray = allInfo.split(',')

			karoserija = infoArray[0]

			#Limuzina 0
			#Hecbek   1
			#Karavan  2
			#Kupe     3

			if "Limuzina" in karoserija:
				karos = 0
			if "bek" in karoserija:
				karos = 1
			if "Karavan" in karoserija:
				karos = 2
			if "Kupe" in karoserija:
				karos = 3

			gorivo = infoArray[2]

			kw = infoArray[3].split('kW')[0].strip()

			menjacIKlima = infoArray[4]
			#menjac manuelni 0, automatski 1
			#klima manuelna 0, automatska 1
			if "Manuelni" in menjacIKlima:
				menjac = 0
			else:
				menjac = 1
			if "Manuelna" in menjacIKlima:
				klima = 0
			else:
				klima = 1

			try:
				writeF = str(kw) + "," + km + "," + year + ","+ str(klima) + ","+ str(menjac)+","+str(karos) +'\n'
				writeP = price + '\n'

				if ("Manu" and "Auto") not in writeF:
					f.write(writeF)
					p.write(writeP)

			except Exception as e:
				errorFile.write(str(x) + '********' + str(e) + '********' + '\n')
				pass
	x = x +1
f.close
p.close
errorFile.close 