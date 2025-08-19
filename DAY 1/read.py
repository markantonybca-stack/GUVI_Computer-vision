import cv2
import matplotlib.pyplot as plt

img =  cv2.imread("image.jpg")
print(img)

cv2.rectangle(img,(100,100),5100,500),(355,00),3)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
