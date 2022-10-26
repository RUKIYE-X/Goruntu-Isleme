import cv2
import numpy as np
from matplotlib import pyplot as plt


grifoto = cv2.imread("grifoto.png",0)
cv2.imshow("gri foto ",grifoto)
cv2.waitKey()


hist=np.zeros(256)
[w,h]=grifoto.shape
for k in range(h):
    for l in range(w):
         deger = grifoto[l,k]
         hist[deger]=hist[deger]+1


for p in range(256):
    print(p,".pixel -> ",hist[p])



plt.plot(hist)
plt.show()
cv2.waitKey()