import cv2
import urllib.request
import numpy as np

req = urllib.request.urlopen('https://www.illico-travaux.com/wp-content/uploads/2018/02/am%C3%A9nagements-ext%C3%A9rieurs.jpeg')
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv2.imdecode(arr, -1) # 'Load it as it is'

cv2.imshow('lalala', img)
if cv2.waitKey() & 0xff == 27: quit()