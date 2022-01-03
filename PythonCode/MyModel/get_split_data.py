import pandas as pd
data_path = r'data/data.csv'
df = pd.read_csv(data_path)
print('data frame size:', len(df))

X_labels = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'DEM', 'NDVI', 'NDWI']
# X_labels = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7']
y_label = 'label'

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df[X_labels], df[y_label], test_size=0.1, stratify=df['label'], random_state=15)
# X_train, X_test, y_train, y_test = train_test_split(df[X_labels], df[y_label], test_size=0.2, stratify=df['label'], random_state=15)
print('X_train size:', len(X_train), '| X_test size:', len(X_test), '| y_train size:', len(y_train), '| y_test size:', len(y_test))
print('-'*80)