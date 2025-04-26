import cv2
import mediapipe as mp


# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7, model_complexity=0)
mp_drawing = mp.solutions.drawing_utils

# Initialize OpenCV webcam
cap = cv2.VideoCapture(0) 
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()
else:
    print("Camera opened successfully.")

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
cap.set(cv2.CAP_PROP_FPS, 15) 




while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue

    # Convert the BGR image to RGB and process it with MediaPipe
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)

    finger_count = 0

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get hand landmarks (21 points)
            landmarks = hand_landmarks.landmark

            # Finger tip landmarks (index, middle, ring, pinky, thumb)
            finger_tips = [8, 12, 16, 20]
            thumb_tip = 4

            # Count raised fingers (excluding thumb)
            for tip in finger_tips:
                if landmarks[tip].y < landmarks[tip - 2].y:  # Compare with joint below
                    finger_count += 1

            # Check thumb (different logic due to thumb's rotation)
            thumb_up = landmarks[thumb_tip].x > landmarks[thumb_tip - 1].x  # For right hand
            if thumb_up:
                finger_count += 1



    cv2.putText(image, f"Fingers: {finger_count}", (10, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Hand Tracking', image)

    # Exit on 'q' key press or X icon
    if cv2.waitKey(5) & 0xFF == ord('q') or cv2.getWindowProperty('Hand Tracking', cv2.WND_PROP_VISIBLE) < 1:
        break
    
cap.release()
cv2.destroyAllWindows()
