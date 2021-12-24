from osgeo import gdal
import numpy as np
import pandas as pd

data_path = 'data.csv'

img_path = r'../../Data/UTM/MDA_2019.tif'

import getPixels
map_path = 'map.csv'

df = pd.read_csv(data_path)
map_df = pd.read_csv(map_path)
X_labels = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'DEM', 'NDVI', 'NDWI']
y_label = 'label'

# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression(random_state=10, solver='newton-cg')
# modelname = 'LR'

# from sklearn.naive_bayes import GaussianNB
# model = GaussianNB()
# modelname = 'GNB'

from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(criterion='entropy', max_features='auto', n_estimators=150, random_state=110)
modelname = 'RFC'

# from sklearn.svm import SVC
# model = SVC(C=1, degree=3, kernel='poly', random_state=10, tol=0.01)
# modelname = 'SVM'

model.fit(df[X_labels], df[y_label])

map_df['pred'] = model.predict(map_df[X_labels])
map_df = map_df[['rows', 'cols', 'pred']]
print(map_df)

ds = gdal.Open(img_path, gdal.GA_ReadOnly)
data = ds.ReadAsArray()
bands, rows, cols = data.shape

output_map = np.zeros(shape=(rows, cols), dtype=np.float32) + 255
for lines in map_df.values:
    i, j, pred = lines
    output_map[int(i)][int(j)] = pred

outfname ='MienBac.'+modelname+'.tif'
driver = gdal.GetDriverByName("GTiff")
dst_ds = driver.Create(outfname, cols, rows, 1, gdal.GDT_Float32)
dst_ds.SetGeoTransform(ds.GetGeoTransform())
dst_ds.SetProjection(ds.GetProjection())
band = dst_ds.GetRasterBand(1)
band.SetNoDataValue(255)
band.WriteArray(output_map)
dst_ds = None
