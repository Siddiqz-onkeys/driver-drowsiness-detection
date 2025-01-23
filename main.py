import cv2 #for video and image capturing
import dlib 
import imutils
from scipy.spatial import distance #to calculate the distance between the points
from imutils import face_utils #to process the image
from pygame import mixer #To play music

mixer.init()
mixer.music.load("your music file")

def eye_aspect_ratio(eye):
    A=distance.euclidean(eye[1],eye[5])#vertical distance
    B=distance.euclidean(eye[2],eye[4])#vertical distance
    C=distance.euclidean(eye[0],eye[3])#horizontal distance
    ear=(A+B)/(2.0*C)
    return ear


tresh=0.25
flag=0 #frame count
frame_check=20 #It is the reference point of how many frames should be the peak point
#defining the facial points of left and right eyes    
(lStart,LEnd)=face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart,rEnd)=face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]

detect=dlib.get_facial_face_detector() #to detect the face 
predict=dlib.shape_predictor("shape_predector_68_face_landmarks.dat") #its a pre-trained model to identify all the 68 spots on our face
#we will calculate the Eye Aspect RAtio using the these facial points when this value is lower than a threshold for a certian period of time we can detect closed eyes

#P0-P5  circular serieal numbers || P0-P3 horizontal distance

cap=cv2.VideoCapture(0) #uses the in-built cam to capture the video

while True:
    ret,frame=cap.read() #this returns two values 1.boolean variable if the frame is available or not 2.image frame 
    frame=imutils.resize(frame,width=450) #resizing the frame to get a small window

    
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #converting into grascake frame
    subjects=detect(gray,0)
    for subject in subjects:
        shape=predict(gray,subjects)
        shape=face_utils.shape_to_np(shape)#converting shape into an x-y cordinate format for all the identified shaped
        leftEye=shape[lStart:LEnd]
        rightEye=shape[rStart:rEnd]
        leftEar= eye_aspect_ratio(leftEye)
        rightEar= eye_aspect_ratio(rightEye)
        ear=(leftEar+rightEar)/2.0
        #convexHull is the minim boundary that the object should completely get wrapoped up
        leftEyeHull=cv2.convexHull(leftEye)
        rightEyeHull=cv2.convexHull(rightEye)
        #contors is the curve that joins all the points that are on the boundary of the object
        cv2.drawContoure(frame,[leftEyeHull], -1, (0, 255,0),1) #contour(image,actual_contour,co-ordinates[we are using all the poiints so negative values does the job],color,thickness)
        cv2.drawContoure(frame,[rightEyeHull],-1,(0,255,0),1)
        if ear>tresh:
            flag+=1
            print(flag)#we can use the warning message or music
            #there the problem is even when the user blinks the eye ear will be less than the tresh so we use the frames 
            if flag>frame_check:
                cv2.putTExt(frame,"*****Alertttttttt*******",(10,30),cv2.Font_HERSHEY_SIMPLEX,0.7,(0,0,255,2))
                mixer.music.play() #plays the sound            
            else:
                flag==0
                
                
        
        
        
    cv2.imshow("frame",frame)#shoqws the frame its capturing
    if cv2.waitKey(1) & 0xFF== ord("q"):
        break
cv2.destroyAllWindows()
cap.release()
    
     
 