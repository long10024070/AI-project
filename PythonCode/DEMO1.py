from osgeo import gdal, ogr, os, osr    # import mấy cái này là để dùng gdal
import numpy as np  # import cái này là để dùng gdal
import shutil   # import cái này để xử lý file, không liên quan đến xử lý dữ liệu

data_path = "../Data/GEE_DATA/MODIS_Aqua_2019_scale500.tif"

ds = gdal.Open(data_path, gdal.GA_ReadOnly)

data = ds.ReadAsArray()

geotransform = ds.GetGeoTransform()
# print(data)
print(data.shape)
print(geotransform)

# Cái này cài đơn giản, nhưng chỉ dùng khi file đầu và và đầu ra có cùng kích thước
# output_path: Đường dẫn file đầu ra
# data_path: Đường dẫn file đầu vào
# newarr: Mâ trận truyền vào file output
def newDatasetWithSameSize(output_path, data_path, newarr):
    output_path = "../Data/Output/test.tif"
    shutil.copy(data_path, output_path)
    ds = gdal.Open(output_path, gdal.GA_Update)
    ds.GetRasterBand(1).WriteArray(newarr) # Số 1 ở đây là lấy dữ liệu ở band thứ 1

# Cái này cài khó hơn, nhưng chắc chắn đúng, code mẫu rồi
# newRasterfn: Đường dẫn file đầu ra
def array2raster(newRasterfn,rasterOrigin,pixelWidth,pixelHeight,array):

    cols = array.shape[1] # Lấy số cột, hàng của ma trận
    rows = array.shape[0]
    originX = rasterOrigin[0] # Tọa độ gốc - điểm trái trên của map
    originY = rasterOrigin[1]

    driver = gdal.GetDriverByName('GTiff')
    outRaster = driver.Create(newRasterfn, cols, rows, 1, gdal.GDT_Byte) # 1 là số band trong ảnh output
    outRaster.SetGeoTransform((originX, pixelWidth, 0, originY, 0, pixelHeight)) # nhập thông số cho map
    outband = outRaster.GetRasterBand(1) # 1 ở đây là lấy dữ liệu từ band thứ 1
    outband.WriteArray(array)
    outRasterSRS = osr.SpatialReference() # Dòng này và 2 dưới dưới là để set hệ quy chiếu cho ảnh tif
    outRasterSRS.ImportFromEPSG(32648) # Cái này là mã khu vực mình chọn ở hệ quy chiếu UTM - WGS_1984_UTM_Zone_48N
    outRaster.SetProjection(outRasterSRS.ExportToWkt())
    outband.FlushCache()