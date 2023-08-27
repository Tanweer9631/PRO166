import cv2
img=cv2.imread("poster.jpg")
rocket=img[120:360,400:500]
img[0:240,500:600]=rocket
my_text="Tanweer"
cv2.putText(img,my_text,(140,200),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=2,color=(255,0,0))
gray_img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("poster", gray_img)
cv2.waitKey(0)
print(img)