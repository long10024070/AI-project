from get_split_data import X_test, X_train, y_test, y_train

print('Running Support Vector Machine Model')

foldCV = 10
score = 'accuracy'

# ###
# import numpy as np
# from sklearn.svm import SVC
# from sklearn.model_selection import cross_val_score, StratifiedKFold
# svm = SVC(kernel="linear", C=0.025, random_state=101)
# skf = StratifiedKFold(n_splits=foldCV, shuffle=True, random_state=12)
# cv_scores = cross_val_score(svm, X_train, y_train, cv=skf, scoring=score)
# print(score,'score -',foldCV,'foldCV - Training dataset: {}'.format(np.mean(cv_scores)))
#
# svm.fit(X_train, y_train)
# y_pred=svm.predict(X_test)
# exit(0)

### Find best paramenter
from sklearn.svm import SVC
from sklearn.model_selection import StratifiedKFold, GridSearchCV

svm = SVC(C=0.025)
skf = StratifiedKFold(n_splits=foldCV, shuffle=True, random_state=12)
param_grid = {
    'kernel': ['sigmoid', 'poly', 'rbf'],
    'random_state': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120],
    'C' : [0.01, 0.1, 1, 10],
    'degree': [2,3,4],
    'tol': [1e-3, 1e-4, 1e-2]
}

gridCV_clf = GridSearchCV(estimator = svm, param_grid=param_grid, cv = skf, scoring='accuracy', verbose=2)
gridCV_clf.fit(X_train, y_train)
print(gridCV_clf.best_params_)
print(gridCV_clf.best_score_)

# ###
# from sklearn.svm import SVC
# svm = SVC(max_features='auto', n_estimators=100, random_state=80, criterion='gini')
# svm.fit(X_train,y_train)
# y_pred=svm.predict(X_test)
#
# from sklearn.metrics import accuracy_score, confusion_matrix
# print('Accuracy score - Test dataset: {}'.format(accuracy_score(y_test, y_pred)))