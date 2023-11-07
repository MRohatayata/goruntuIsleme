import cv2
from dizinSettings import getParentFolder

parentFolder = getParentFolder()
resim = parentFolder + "resimler\\kurtResmi.jpg"

resim = cv2.imread(resim, 0)

cv2.imshow("kurtcuk :)", resim)
histogram = [0] * 256
for i in range(len(resim)):
    for j in range(len(resim[0])):
        gray_value = resim[i, j]
        histogram[gray_value] += 1

for gray_level, count in enumerate(histogram):
    print(f"Gri Değer: {gray_level}, Piksel Sayısı: {count}, {'*' * (count // 10)}")

cv2.waitKey(0)
cv2.destroyAllWindows()