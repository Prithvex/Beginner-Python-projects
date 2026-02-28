#This is main python face detection file 
"""In this project I'll do the face detction using pyhon

-- camera access -- hollow rectangular box -- 
-- initialise the environment and download the libraries
1. OpenCv-- pip install opencv-python
2. haarcascade_frontalface_default.xml
--- download from web 
    """
 
import cv2 

a = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#allow access to our camera
#0 means default camera
b= cv2.VideoCapture(0)

while True:
    
    #This reads the frame of camera 
    c_rect, d_img= b.read()
    
    #This convert an image into Black-white format for fast detection
    e = cv2.cvtColor(d_img, cv2.COLOR_BGR2GRAY)
    
    # Detect Faces
    f= a.detectMultiScale(e, 1.3, 6)
    
    # Draw Rectanglq Around Faces
    for (x1, y1, w1, h1) in f:
        cv2.rectangle(d_img, (x1, y1), (x1+w1, y1+h1), (255, 0, 0), 5 )
        
        cv2.imshow('Mukhda', d_img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        # Press q to stop
        
b.release()
cv2.destroyAllWindows






