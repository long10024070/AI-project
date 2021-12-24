from get_split_data import X_test, X_train, y_test, y_train

print('Running Random Forest Model')

# import numpy as np
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import cross_val_score, StratifiedKFold
# clf=RandomForestClassifier(n_estimators=100, random_state=9)
# skf = StratifiedKFold(n_splits=10, shuffle=True,random_state=12)
# cv_scores = cross_val_score(clf, X_train, y_train, cv=skf, scoring='accuracy')
# print('Accuracy score - 10foldCV - Training dataset: {}'.format(np.mean(cv_scores)))
# exit(0)

### Find best paramenter
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, GridSearchCV

clf=RandomForestClassifier()#(random_state=9)
skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=12)
param_grid = {
    'n_estimators': [150],
    'random_state': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120],
    'max_features': ['auto', 'sqrt', 'log2'],
    'criterion' : ['gini','entropy'],
}

gridCV_clf = GridSearchCV(estimator = clf, param_grid=param_grid, cv = skf, scoring='accuracy', verbose=2)
gridCV_clf.fit(X_train, y_train)
print(gridCV_clf.best_params_)
print(gridCV_clf.best_score_)

# ###
# from sklearn.ensemble import RandomForestClassifier
# clf = RandomForestClassifier(max_features='auto', n_estimators=100, random_state=80, criterion='gini')
# clf.fit(X_train,y_train)
# y_pred=clf.predict(X_test)
#
# from sklearn.metrics import accuracy_score, confusion_matrix
# print('Accuracy score - Test dataset: {}'.format(accuracy_score(y_test, y_pred)))
