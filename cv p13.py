import cv2
import numpy as np
cap = cv2.VideoCapture("D:\open cv\WhatsApp Video 2024-03-25 at 9.00.31 AM.mp4")
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
src_points = np.float32([[0, 0], [width - 1, 0], [0, height - 1], [width - 1, height - 1]])
dst_points = np.float32([[0, 0], [width - 1, 0], [0, height - 1], [width - 150, height - 1]])
M = cv2.getPerspectiveTransform(src_points, dst_points)
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
       
        warped_frame = cv2.warpPerspective(frame, M, (frame.shape[1], frame.shape[0]))
        cv2.imshow('Warped Frame', warped_frame)
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
