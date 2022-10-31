import cv2
import numpy as np


goruntu = cv2.imread('grikafa.png',0)

"""
negatif görüntüye dönüştürmeninm hazır kodu

tersGoruntu = np.invert(goruntu)
cv2.imshow("orjinal",goruntu)
cv2.imshow("ters goruntu",tersGoruntu)
cv2.waitKey() 
"""
cv2.imshow("Orjinal Goruntu",goruntu)

negGoruntu = 255 - goruntu
cv2.imshow("Negatif Goruntu",negGoruntu)
cv2.waitKey()


[x,y] = goruntu.shape
yenigoruntu = np.zeros([x,y], dtype=np.uint8)
for i in range(x):
    for j in range(y):
        yenigoruntu[i,j] = 255 - goruntu[i,j]

print(goruntu[0,0]) #görüntünün max pixeli




