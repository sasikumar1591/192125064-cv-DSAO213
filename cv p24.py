import cv2
import numpy as np
img = cv2.imread("D:\open cv\Picture4.png")
if img is None:
    print("Error: Image not loaded.")
else:    
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
    blurred_img = cv2.GaussianBlur(gray_img, (0, 0), 3) 
    unsharp_mask = cv2.subtract(gray_img, blurred_img)
    sharpened_img = cv2.addWeighted(gray_img, 1.5, unsharp_mask, -0.5, 0)
    sharpened_img_bgr = cv2.cvtColor(sharpened_img, cv2.COLOR_GRAY2BGR)
    cv2.imshow('Original Image', img)
    cv2.imshow('Sharpened Image', sharpened_img_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
