# Xử lý dữ liệu của tọa độ mẫu
# Nhận vào tọa độ mẫu (x, y) từ file data_path,
# tính ra chỉ số của tọa độ tại tất cả các band của file MIEN_BAC_data_path và chỉ số NDVI, NDWI.
# Dữ liệu sau khi tính toán xong được xuất ra file output_data_path.
# Lưu ý: các band trong code được đánh số từ 0 tới 6 thay vì từ 1 tới 7 dưới dạng bảng .csv
# END

from osgeo import gdal, ogr, os, osr
import numpy as np
import shutil
import os
import progressbar
import math

data_path = "../Data/SampleData/#sample.txt"
MIEN_BAC_data_path = "../Data/UTM/MDA_2019.tif"
output_data_path = "../Data/SampleData/#sample_detail.csv"

data = open(data_path, "r")
mienbac = gdal.Open(MIEN_BAC_data_path, gdal.GA_ReadOnly)
red = 0
nir = 1
green = 3
blue = 2
outfile = open(output_data_path, "w")

mienbac_data = mienbac.ReadAsArray()
mienbac_geoTrans = mienbac.GetGeoTransform()
originX = mienbac_geoTrans[0]
pixelWidth = mienbac_geoTrans[1]
originY = mienbac_geoTrans[3]
pixelHeight = mienbac_geoTrans[5]
# print(originX, originY, pixelWidth, pixelHeight)

if (data.readable()):
    data.readline()
    tableheader = "X, Y, label, Band_1, Band_2, Band_3, Band_4, Band_5, Band_6, Band_7, NDVI, NDWI, \n"
    outfile.write(tableheader)
    while (True):
        line = data.readline()
        if not line:
            break
        a = line.split()
        x = y = 0
        label = "NA"
        if (len(a) >= 3):
            x = float(a[0])
            y = float(a[1])
            label = a[2]
        else:
            continue
        # print(x, y, label)
        tablerow = str(x) + ", " + str(y) + ", " + label + ", "
        col_id = math.floor((x-originX) / pixelWidth)
        row_id = math.floor((y-originY) / pixelHeight)
        for i in range (len(mienbac_data)):
            # print(mienbac_data[i][row_id][col_id])
            tablerow += str(mienbac_data[i][row_id][col_id]) + ", "
        NDVI = (mienbac_data[nir][row_id][col_id] - mienbac_data[red][row_id][col_id]) / (mienbac_data[nir][row_id][col_id] + mienbac_data[red][row_id][col_id])
        NDWI = (mienbac_data[green][row_id][col_id] - mienbac_data[nir][row_id][col_id]) / (mienbac_data[green][row_id][col_id] + mienbac_data[nir][row_id][col_id])
        tablerow += str(round(NDVI,3)) + ", " + str(round(NDWI,3)) + ", "
        tablerow += "\n"
        # print(tablerow)
        outfile.write(tablerow)
else:
    print("Error")

data.close()
outfile.close()