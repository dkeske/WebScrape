import numpy as np 
from sklearn import linear_model, datasets

f = open("outputfilePOLOVNI.txt")
g = open("outputfilePOLOVNIcena.txt")
h = open("ocena.txt", "w")

dataParams = np.loadtxt(f, delimiter=',')
dataPrice = np.loadtxt(g)
#odnos 70:30
dataParams_train = dataParams[:-200]
dataParams_test = dataParams[-200:]

dataPrice_train = dataPrice[:-200]
dataPrice_test = dataPrice[-200:]

#clf = linear_model.LinearRegression(normalize=True)
clf = linear_model.Ridge (alpha = .3, normalize=True)
clf.fit(dataParams_train, dataPrice_train)

print(np.mean(clf.predict(dataParams_test)-dataPrice_test)**2)
print("Koeficijenti: ")
print(clf.coef_)
print("Konstanta: ")
print(clf.intercept_)
#print("Razlika: ")
#print(clf.predict(dataParams_test)-dataPrice_test)
np.savetxt(h, clf.predict(dataParams_test)-dataPrice_test, fmt='%.2f')
#recall, precision accuracy