import cv2
import numpy as np
cap = cv2.VideoCapture("D:\open cv\WhatsApp Video 2024-03-25 at 9.00.31 AM.mp4")
if (cap.isOpened()== False):
 print("Error opening video file")
while(cap.isOpened()):
 ret, frame = cap.read()
 if ret == True:
  cv2.imshow('Frame', frame)
  if cv2.waitKey(250) & 0xFF == ord('q'):
   break
 else:
  break
cap.release()
cv2.destroyAllWindows()
