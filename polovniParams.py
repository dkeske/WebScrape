

def calculatePrice(kw, km, year, ac, gears, body):
	import numpy as np 
	from sklearn import linear_model, datasets
	f = open("outputfilePOLOVNI.txt")
	g = open("outputfilePOLOVNIcena.txt")
	h = open("ocena.txt", "w")

	dataParams = np.loadtxt(f, delimiter=',')
	dataPrice = np.loadtxt(g)
	clf = linear_model.Ridge (alpha = .3, normalize=True)
	clf.fit(dataParams, dataPrice)
	prediction = clf.predict([kw, km, year, ac, gears, body])
	return prediction