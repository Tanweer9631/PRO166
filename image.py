import numpy as np
import cv2
black_bg= np.ones([600,600])
black_bg[200:400,200:400]=255
cv2.imshow("blackbg", black_bg)
cv2.waitKey(0)
print(black_bg)