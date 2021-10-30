from osgeo import gdal, ogr, os, osr    # import mấy cái này là để dùng gdal
import numpy as np  # import cái này là để dùng gdal
import shutil   # import cái này để xử lý file, không liên quan đến xử lý dữ liệu
import math
from array import array

data_path = "../Data/UTM/MDA_2019.tif"

if data_path is None:
    print ('Unable to open file .tif')
    sys.exit(1)

raster = gdal.Open(data_path, gdal.GA_ReadOnly)

RasterCount = raster.RasterCount

print("[ RASTER BAND COUNT:    ", RasterCount)


for band in range(1, RasterCount+1):    
    ar = raster.GetRasterBand(band).ReadAsArray().astype('float')
    summ = 0.0
    arr = []
    for x in np.nditer(ar):
        if (x >= 50 and x <= 10000):
            summ += x
            arr.append(x)
    std = 0.0
    arr.sort()
    mean = summ/len(arr)
    for i in range(len(arr)):
        std = std + pow((arr[i]- mean), 2)/(len(arr) - 1)   
    print(std)        
    print("[ BAND ]: ", band)
    print ("[ STATS ] =   Maximum = %s, Minimum = %s, Median = %s, Mean = %s, Std = %s, " 
    % (round(float(arr[len(arr) - 1]), 2), round(float(arr[0]), 2), round(float(arr[len(arr) // 2]), 2), 
    round(mean, 2), round(math.sqrt(std), 2)))

    