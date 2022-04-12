import cv2

vid = cv2.VideoCapture('AnthonyShkraba.mp4')
if vid.isOpened() == False:
    print('Unable to open the camera.')

height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(vid.get(cv2.CAP_PROP_FPS))

print(height, width, fps)

output = cv2.VideoWriter('Boxing.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 30, (width, height))

while (True):
    ret,frame = vid.read()
    cv2.imshow('Webcam', frame)
    output.write(frame)
    if cv2.waitKey(25) == 32:
        break
vid.release()
output.release()
cv2.destroyAllWindows() 