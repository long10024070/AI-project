from get_split_data import X_test, X_train, y_test, y_train

###
from sklearn.naive_bayes import GaussianNB
nb = GaussianNB()
nb.fit(X_train,y_train)
y_pred=nb.predict(X_test)

from sklearn.metrics import accuracy_score, confusion_matrix
print('Accuracy score - Test dataset: {}'.format(accuracy_score(y_test, y_pred)))