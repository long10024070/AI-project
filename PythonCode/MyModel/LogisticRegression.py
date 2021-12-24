from get_split_data import X_test, X_train, y_test, y_train

### Find best paramenter
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold, GridSearchCV

lr = LogisticRegression()
skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=12)
param_grid = {
    'random_state': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120],
    'solver': ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga']
}

gridCV_clf = GridSearchCV(estimator = lr, param_grid=param_grid, cv = skf, scoring='accuracy', verbose=2)
gridCV_clf.fit(X_train, y_train)
print(gridCV_clf.best_params_)
print(gridCV_clf.best_score_)

# ###
# from sklearn.linear_model import LogisticRegression
# lr = LogisticRegression()
# lr.fit(X_train,y_train)
# y_pred=lr.predict(X_test)
#
# from sklearn.metrics import accuracy_score, confusion_matrix
# print('Accuracy score - Test dataset: {}'.format(accuracy_score(y_test, y_pred)))