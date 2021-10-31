# getLandcoverSize(data_path):
#       Trả về số pixel của mỗi phân lớp trong bản đồ

# calculateSampleNumber(totalSample, ratio):
#       Tính số mẫu phải lấy cho mỗi phân lớp
#       sao cho tổng số lượng mẫu được lấy là totalSample
#       và tỉ số của mỗi số mẫu so với totalSample sẽ tương ứng với tỉ lệ có thứ tự tương ứng trong mảng ratio.
#       Nhận xét: Nếu chọn ratio theo tỉ lệ số pixel/(tổng số pixel thuộc các phân lớp này trong ảnh)
#       cách chọn số lượng mẫu cho mỗi phân lớp này không hợp lý lắm
#       do có những phân lớp vẫn vó pixel nhưng tỉ lệ rất nhỏ,
#       khi tính ra thì kết quả rất nhỏ (bằng 1 khi totalSample = 10k)

# calculateSampleNumber_advance(minval, totalsample, landcoverSize):
#       Tính số mẫu phải lấy cho mỗi phân lớp
#       sao cho tổng số lượng mẫu được lấy là totalsample
#       số mẫu nhỏ nhất được lấy cho một phân lớp có pixel trong ảnh gốc bằng minval.
#       Đồng thời phải đảm bảo tỉ số delta của số mẫu của 2 phân lớp có số mẫu khác 0
#       là không đổi so với delta của số pixel (đã được tính trong mảng landcoverSize)
#       Nhận xét: Có vẻ như cách này sẽ giúp các phân lớp có số lượng pixel nhỏ vẫn lấy được đủ
#       số mẫu cần thiết để lập bản đồ trong khi vẫn đảm bảo được tính tổng thể so với các phân lớp khác
#       tuy nhiên, vẫn chưa chọn được minval hợp lý cho totalsample = 2000

from osgeo import gdal, ogr, os, osr    # import mấy cái này là để dùng gdal
import numpy as np  # import cái này là để dùng gdal
import progressbar

default_data_path = "../Data/RAW_DATA/MIEN_BAC_real.tif"
default_ratio = [0,1] + [0] * 30

def getLandcoverSize(data_path):
    ds = gdal.Open(data_path, gdal.GA_ReadOnly)
    data = ds.ReadAsArray()
    print("Số pixel của mỗi phân lớp:")
    count = [0] * 11
    bar = progressbar.ProgressBar(max_value=len(data)).start()
    cnt = 0
    for row in data:
        for val in row:
            if (val != 0) & (val != 255):
                id = 0
                if (val == 1) | (val == 2):
                    id = 1
                if (val == 3):
                    id = 2
                if (val >= 4) & (val <= 6):
                    id = 3
                if (val == 7):
                    id = 4
                if (val == 8):
                    id = 5
                if (val == 9):
                    id = 6
                if (val == 10) | (val == 11) | (val == 12) | (val == 14) | (val == 20):
                    id = 7
                if (val == 15):
                    id = 8
                if (val == 18):
                    id = 9
                if (val == 19):
                    id = 10
                if (1 <= id) & (id <= 19):
                    count[id] += 1
        cnt += 1
        bar.update(cnt)
    bar.finish()
    for i in range(1, len(count)):
        print("Phân lớp", i, "được biểu diễn với", count[i] , "pixel")
    print("\n\n")
    return count

def calRatio(landcoverSize):
    ratio = landcoverSize.copy()
    total = 0
    for val in ratio:
        total += val
    if (total == 0):
        print("\nError, no pixel counted\n")
        exit(2)
    for i in range(len(ratio)):
        ratio[i] = round(ratio[i] / total, 4)
    return ratio

def calculateSampleNumber(totalSample, ratio):
    print("Sử dụng", totalSample, "mẫu")
    nsample = ratio.copy()
    for i in range(len(nsample)-1):
        nsample[i] = round(nsample[i] * totalSample)
    for i in range(len(nsample)-1):
        totalSample -= nsample[i]
    nsample[len(nsample)-1] = totalSample
    print("resident:", nsample[1], "mẫu, chiếm tỉ lệ", ratio[1] * 100, "%")
    print("rice:", nsample[2], "mẫu, chiếm tỉ lệ", ratio[2] * 100, "%")
    print("crop:", nsample[3], "mẫu, chiếm tỉ lệ", ratio[3] * 100, "%")
    print("grass:", nsample[4], "mẫu, chiếm tỉ lệ", ratio[4] * 100, "%")
    print("barren:", nsample[5], "mẫu, chiếm tỉ lệ", ratio[5] * 100, "%")
    print("scrub:", nsample[6], "mẫu, chiếm tỉ lệ", ratio[6] * 100, "%")
    print("forest:", nsample[7], "mẫu, chiếm tỉ lệ", ratio[7] * 100, "%")
    print("wet:", nsample[8], "mẫu, chiếm tỉ lệ", ratio[8] * 100, "%")
    print("water:", nsample[9], "mẫu, chiếm tỉ lệ", ratio[9] * 100, "%")
    print("aqua:", nsample[10], "mẫu, chiếm tỉ lệ", ratio[10] * 100, "%")
    print("\n\n")

def calculateSampleNumber_advance(minval, totalsample, landcoverSize):
    print("Sử dụng", totalsample, "mẫu, minval:", minval)
    nsample = landcoverSize.copy()
    totalval = 0
    min = -1
    for val in nsample:
        if (val != 0) & ((val < min) | (min == -1)):
            min = val
    for i in range(len(nsample)):
        nsample[i] -= min
        if (nsample[i] >= 0):
            totalval += nsample[i]
            totalsample -= minval
    for i in range(len(nsample)):
        if (nsample[i] >= 0):
            nsample[i] = round(nsample[i] / totalval * totalsample)
    for i in range(len(nsample)-1):
        if (nsample[i] >= 0):
            totalsample -= nsample[i]
            nsample[i] += minval
        else:
            nsample[i] = 0
    nsample[len(nsample)-1] = minval + totalsample
    print("resident:", nsample[1])#, "mẫu, chiếm tỉ lệ", ratio[1] * 100, "%")
    print("rice:", nsample[2])#, "mẫu, chiếm tỉ lệ", ratio[2] * 100, "%")
    print("crop:", nsample[3])#, "mẫu, chiếm tỉ lệ", ratio[3] * 100, "%")
    print("grass:", nsample[4])#, "mẫu, chiếm tỉ lệ", ratio[4] * 100, "%")
    print("barren:", nsample[5])#, "mẫu, chiếm tỉ lệ", ratio[5] * 100, "%")
    print("scrub:", nsample[6])#, "mẫu, chiếm tỉ lệ", ratio[6] * 100, "%")
    print("forest:", nsample[7])#, "mẫu, chiếm tỉ lệ", ratio[7] * 100, "%")
    print("wet:", nsample[8])#, "mẫu, chiếm tỉ lệ", ratio[8] * 100, "%")
    print("water:", nsample[9])#, "mẫu, chiếm tỉ lệ", ratio[9] * 100, "%")
    print("aqua:", nsample[10])#, "mẫu, chiếm tỉ lệ", ratio[10] * 100, "%")
    total = 0
    for val in nsample:
        total += val
    print(total,"\n\n")

def getSampleNumber():
    nSamples = [500, 750, 1000, 2000]
    minvalList = [50, 75, 100]
    print(nSamples,'\n')
    # landcoverSize = getLandcoverSize(default_data_path)
    # Đây là kết quả đã tính được khi dùng dữ liệu từ bản đồ phân lớp Việt Nam được cho (đã cắt khu vược ĐBSH)
    landcoverSize = [0, 971677, 2725678, 2731169, 165829, 85450, 1535, 2885826, 0, 586004, 191926]
    ratio = calRatio(landcoverSize)
    for minval in minvalList:
        for nsample in nSamples:
            # calculateSampleNumber(nsample, ratio)
            calculateSampleNumber_advance(minval, nsample, landcoverSize)

getSampleNumber()

