## [Video](https://drive.google.com/drive/u/1/folders/1awGYqGV_5hWIoVv1vNOF4-kRdxzHxZOe?fbclid=IwAR11ad05Ecp6A2AnpCRYWFspzNdUBTHvQbV9xpSIRWxhRZE6F1sttR5NC1I)
## [Nội dung các tuần của thầy](https://drive.google.com/drive/u/1/folders/1JJwqWC6EleRNKuATofdjEKSIjEiy3iF5?fbclid=IwAR2u54f6pQVvyxwTa4wJeakeqZPQfrEdAxA058Zu_eAsTQAgKxoVucr99No)
## [Drive làm việc nhóm](https://drive.google.com/drive/folders/1BUWctrc0WJH_nWLLlUhdlkYShLVwuAOe?usp=sharing)

# Week 3

### Thông tin trong các loại band trong map VLUCD
1. Phân lớp 1, 2: đất ở (residential land) - resident - OK
2. Phân lớp 3: đồng lúa (rice paddies) - rice - OK
3. Phân lớp 4, 5, 6: đất trồng trọt (croplands) - crop - OK
4. Phân lớp 7: đồng cỏ (grassland) - grass - OK
5. Phân lớp 8: đất cằn cỗi (barren land) - barren - OK
6. Phân lớp 9: bụi rậm (scrub/shrub) - scrub - OK
7. Phân lớp 10, 11, 12, 14, 20: rừng (forest) - forest - OK
8. Phân lớp 15: vùng đất trũng, ẩm ướt (wetland) - wet - Không có cái nào
9. Phân lớp 18: vùng nước bỏ trống (open water) - water - OK
10. Phân lớp 19: vùng nước nuôi trồng thủy sản (aquaculture) - aqua - OK

### Sử dụng 2000 mẫu, minval: 75
1. resident: 199
2. rice: 424
3. crop: 425
4. grass: 96
5. barren: 86
6. scrub: 75
7. forest: 445
8. wet: 0
9. water: 150
10. aqua: 100

### Các file shapefile để sử dụng trong GoogleEarth nằm ở thư mục DATA/GEarthSample
1. resident: 199 (anh Long)
2. rice1: 400 (anh Dương)
3. rice2: 24 (anh Long)
4. crop1: 400 (anh Khánh)
5. crop2: 25 (anh Long)
6. grass: 96 (Minh)
7. barren: 86 (Minh)
8. scrub: 75 (Minh)
9. forest1: 400 (Lương Đạt)
10. forest2: 45 (Minh)
11. water: 150 (anh Long)
12. aqua: 100 (Minh)

# Week 2

**[Video buổi họp tuần 2](https://drive.google.com/file/d/1JKutNBoCeaeKwpW9ne3T-aaO8tC5eBDG/view?usp=sharing)**

**Thống nhất là toàn bộ data (ngoại trừ data tải về từ GEE) sẽ dùng hệ quy chiếu UTM**

[Bảng hệ quy chiếu UTM và code của nó (cái này cho vui thôi, thêm vào báo cáo cũng hay)](https://resources.arcgis.com/en/help/main/10.1/018z/pdf/projected_coordinate_systems.pdf)

### Các việc cần làm tuần 2
- Cài đặt Python, gdal, numpy
- Đọc file ảnh vệ tinh đã được tải về, đổi hệ quy chiếu sang UTM
- Thống kê (max, min, median, mean, std) cho từng band
- Tính toán các chỉ số NDVI, NDWI dựa trên 3 band Red (band 1), Green (band 4), NIR (band 2)
- Xuất bản đồ NDVI, NDWI dưới dạng tif
- Hiển thị bản đồ trên arcmap
- [Phân chia công việc](https://docs.google.com/document/d/11A478eDmFSBcSOaOr3UuztbsetMSCNdmQ6gLidZrzT0/edit?usp=sharing)
- [Viết báo cáo tuần 2](https://docs.google.com/document/d/1Hax6q1Zi0FItBQW4oXAlBR-U43D6-dYjsRP-I0aAarM/edit?usp=sharing)

### Hướng dẫn cài đặt python 3.10
1. Vào [link](https://www.python.org/downloads/) và chọn **Download Python 3.10.0** để tải file cài đặt python về
2. Mở bộ cài đặt được tài về, tiến hành cài đặt, nhớ tích chọn cài đặt **PATH** để có thể dùng được python trên cmd, terminal

### Hướng dẫn cài đặt gdal
1. Nhớ cài đặt python trước đó
2. Vào [link](https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal%20t%E1%BA%A3i%20GDAL%E2%80%913.3.2%E2%80%91cp310%E2%80%91cp310%E2%80%91win_amd64.whl)
   1. Tải GDAL‑3.3.2‑cp310‑cp310‑win_amd64.whl dành cho python 3.10, win 64 bit
   2. Tải GDAL‑3.3.2‑cp310‑cp310‑win32.whl dành cho python 3.10, win 32 bit
   3. Không khuyến khích dùng các phiên bản khác nhằm mục đích đồng bộ
3. Tại nơi tải về, mở cmd lên, nhập lệnh sau để cài đặt vào python:


      
      python -m pip install GDAL (ấn thêm phím tab 1 lần để tự động nhảy ra đúng tên file vừa tải về)

### Để code được như code demo của thầy ở buổi 2
Để sử dụng được hàm ReadAsArray(), phải cài đặt thêm numpy, gõ lệnh sau trong cmd hoặc terminal ở đâu cũng được:

    python -m pip install numpy

### Các code mẫu để xử lý ảnh (trong drive của thầy cũng có):
https://pcjericks.github.io/py-gdalogr-cookbook/raster_layers.html

### Xử lý ảnh:
Các ảnh tải xuống từ GEE đang dùng hệ quy chiếu cầu, cần chuyển sang hệ quy chiếu UTM. Cái này không cần code, sử dụng tool Project Raster trong ArcMap là được.

# Week 1
- [Phân chia công việc tuần 1](https://docs.google.com/document/d/18LiRxJy1365zXZHxYvq2JjOhk1iDiqnwuc550IVhdoE/edit?usp=sharing)
- [Báo cáo tuần 1](https://docs.google.com/document/d/1q4bj2tZiTIZd2wr4d2H6bYxeV17nWVYt/edit?usp=sharing&ouid=116186330127070054360&rtpof=true&sd=true)