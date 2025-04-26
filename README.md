Hand Gesture Recognition System
This repository contains two Python scripts for hand gesture recognition using MediaPipe and OpenCV:

analy_hand_gesture.py - Recognizes specific hand gestures (hello, love, like, call, OK, SOS)

fingers_count.py - Counts raised fingers in real-time

Requirements
Python 3.6+

OpenCV (pip install opencv-python)

MediaPipe (pip install mediapipe)

Files Description
1. analy_hand_gesture.py
Recognizes 6 specific hand gestures:

👋 Hello (all fingers raised)

❤️ Love (thumb, index and pinky raised)

👍 Like (thumb up)

📞 Call (pinky and thumb extended)

👌 OK (thumb and index forming circle)

🆘 SOS (specific finger configuration)

Usage:

bash
python analy_hand_gesture.py
Features:

Real-time hand tracking

Multiple gesture recognition

Visual feedback on screen

Press 'c' to exit

2. fingers_count.py
Counts the number of raised fingers in real-time.

Usage:

bash
python fingers_count.py
Features:

Real-time finger counting

Hand landmark visualization

Works with single hand

Press 'q' to exit

How It Works
Both scripts use MediaPipe's hand landmark detection model to track 21 key points on the hand. The positions of these landmarks are analyzed to determine finger positions and gestures.

Configuration
You can adjust these parameters in the scripts:

Camera resolution (width/height)

FPS settings

Detection confidence threshold (in fingers_count.py)

Troubleshooting
If the camera doesn't open:

Check if another application is using the camera

Verify camera permissions

Try changing the camera index (0 to 1) if you have multiple cameras
