from osgeo import gdal
import numpy as np
import pandas as pd
import math

img_path = r'..\..\Data\UTM\MDA_2019.tif'
DEM_data_path = "../../Data/UTM/DEM.tif"

ds = gdal.Open(img_path, gdal.GA_ReadOnly)
red = 0
nir = 1
green = 3
blue = 2
dem_map = gdal.Open(DEM_data_path, gdal.GA_ReadOnly)

data = ds.ReadAsArray()
data_geoTrans = ds.GetGeoTransform()
data_originX = data_geoTrans[0]
data_pixelWidth = data_geoTrans[1]
data_originY = data_geoTrans[3]
data_pixelHeight = data_geoTrans[5]

dem_data = dem_map.ReadAsArray()
dem_geoTrans = dem_map.GetGeoTransform()
dem_originX = dem_geoTrans[0]
dem_pixelWidth = dem_geoTrans[1]
dem_originY = dem_geoTrans[3]
dem_pixelHeight = dem_geoTrans[5]

bands, rows, cols = data.shape

rsl = []
for i in range(rows):
    for j in range(cols):
        if data[0, i, j] > -9999:
            tmp = np.append([i, j], data[:, i, j])
            x = data_originX + (j + 0.5) * data_pixelWidth
            y = data_originY + (i + 0.5) * data_pixelHeight
            DEM = dem_data[math.floor((y-dem_originY) / dem_pixelHeight)][math.floor((x-dem_originX) / dem_pixelWidth)]
            NDVI = (data[nir][i][j] - data[red][i][j]) / (data[nir][i][j] + data[red][i][j])
            NDWI = (data[green][i][j] - data[nir][i][j]) / (data[green][i][j] + data[nir][i][j])
            tmp = np.append(tmp, [DEM, NDVI, NDWI])
            flag = True
            for v in tmp:
                if (math.isnan(v)):
                    flag = False
            if (flag):
                rsl.append(tmp)

df = pd.DataFrame(rsl, columns=['rows', 'cols', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'DEM', 'NDVI', 'NDWI'])
df.to_csv('map.csv', index=False)