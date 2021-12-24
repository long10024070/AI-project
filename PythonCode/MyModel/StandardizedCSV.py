import json
convert_file = open('data\convert.json')
convert = json.load(convert_file)

from osgeo import gdal
import math
MIEN_BAC_data_path = r"D:\Hai Long\Trí tuệ nhân tạo\AI-project\Data\UTM\MDA_2019.tif"
mienbac = gdal.Open(MIEN_BAC_data_path, gdal.GA_ReadOnly)
mienbac_geoTrans = mienbac.GetGeoTransform()
originX = mienbac_geoTrans[0]
pixelWidth = mienbac_geoTrans[1]
originY = mienbac_geoTrans[3]
pixelHeight = mienbac_geoTrans[5]

def standardized_csv(data_file, outdata_file):
    infile = open(data_file, 'r')
    outfile = open(outdata_file, 'w')
    row = 0
    col = 0
    while (1):
        flag = True
        line = infile.readline()
        if line == '':
            break
        col = 0
        thisline = s = ""
        for c in line:
            if (c != ' '):
                if (c != ','):
                    s += c
                else:
                    if row == 0 or col == 2:
                        try: s = convert[s]
                        except: pass
                    if s == 'nan' or s == 'inf':
                        flag = False
                    # if row > 0 and (col == 0 or col == 1):
                    #     s = float(s)
                    #     if col == 0:
                    #         s = math.floor((s-originX) / pixelWidth)
                    #     if col == 1:
                    #         s = math.floor((s-originY) / pixelHeight)
                    #     s = str(s)
                    thisline += s + ','
                    s = ""
                    col += 1
        # print(thisline[0:-1])
        if (flag):
            outfile.write(thisline[0:-1]+'\n')
            row += 1
    infile.close()
    outfile.close()