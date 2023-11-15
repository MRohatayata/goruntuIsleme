from dizinSettings import getParentFolder
import cv2

def findMax(mat) :
    max = mat[0][0]
    for i in range(len(resim)):
        for j in range(len(resim[0])) :
            k = mat[i][j]
            if max < k :
                max = k
    return max


parentFolder = getParentFolder()
resim = parentFolder + "resimler\\kurtResmi.jpg"

resim = cv2.imread(resim,0)

cv2.imshow("kurtcuk :)", resim)
resiMax = findMax(resim)
for i in range(len(resim)):
    for j in range(len(resim[0])) :
        resim[i][j] = resiMax - resim[i][j]
print("Herhangi Bir Tusa Basiniz..")
cv2.waitKey(0)
cv2.imshow("kurtcuk :)", resim)

cv2.waitKey(0)
cv2.destroyAllWindows()
