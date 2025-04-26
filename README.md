# Drowsiness Detection System Using Eye Aspect Ratio (EAR)
This is a real-time drowsiness detection system using a webcam. It detects when the user's eyes remain closed for a specific number of frames and plays an alert sound if drowsiness is detected. This can be useful for driver fatigue detection or general alertness monitoring.

## 🚀🚀 Features
- Real-time facial landmark detection
- Calculates Eye Aspect Ratio (EAR)
- Detects prolonged eye closure (drowsiness)
- Plays an alert sound when drowsiness is detected
 
## 🎯 Requirements
- Python 3.x
- OpenCV
- dlib
- imutils
- scipy
- pygame

## 🤓 HOW It Works
1.	The system uses dlib's facial landmark detector to identify 68 facial landmarks.
2.	It calculates the Eye Aspect Ratio (EAR) using six eye landmarks.
3.	If the EAR falls below a defined threshold for a set number of consecutive frames, the system detects it as a sign of drowsiness.
4.	An alert message is displayed, and an alarm sound is played.


