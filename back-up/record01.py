import cv2
import numpy as np
import urllib

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
        
# Sets up the webcam and connects to it and initalizes a variable we use for it
stream = urllib.urlopen('http://192.168.1.2:8080/video')
bytes=b''

while True:
    # Takes frames from the camera that we can use
    bytes+=stream.read(16384)
    a = bytes.find(b'\xff\xd8')
    b = bytes.find(b'\xff\xd9')
    if a!=-1 and b!=-1:
        jpg = bytes[a:b+2]
        bytes= bytes[b+2:]
        frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),cv2.IMREAD_COLOR)
        out.write(frame)

       # Displays the final product
        cv2.imshow('frame',frame)

     # Hit esc to kill
        if cv2.waitKey(1) ==27:
            exit(0)
