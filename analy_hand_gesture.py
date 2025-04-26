import cv2
import mediapipe as mp
import time

#initialize mediapipe
mphand=mp.solutions.hands
hands=mphand.Hands(static_image_mode=False, max_num_hands=2,model_complexity=0)#model_complexity=0
draw=mp.solutions.drawing_utils


#initialize camera
cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("ERROR, can not open camera")
    exit()
else:
    print("Open camera successfully")


#set frame width, height and fps
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 620)
cap.set(cv2.CAP_PROP_FPS, 20)


output=""
time.sleep(3)
while cap.isOpened():
    success, image=cap.read()
    if not success:
        continue
        
    imageRgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = hands.process(imageRgb)

    

    if result.multi_hand_landmarks:
        for i, hand_landmark in enumerate(result.multi_hand_landmarks):
            #draw hand lanmark
            draw.draw_landmarks(image, hand_landmark, mphand.HAND_CONNECTIONS)

            # get hand landmarks in list
            landmarks=hand_landmark.landmark
            lm0 = landmarks[0]
            lm2 = landmarks[2]
            lm3 = landmarks[3]
            lm4 = landmarks[4]
            lm5 = landmarks[5]
            lm6 = landmarks[6]
            lm7 = landmarks[7]
            lm8 = landmarks[8]
            lm9 = landmarks[9]
            lm10 = landmarks[10]
            lm11 = landmarks[11]
            lm12 = landmarks[12]
            lm13 = landmarks[13]
            lm14 = landmarks[14]
            lm15 = landmarks[15]
            lm16 = landmarks[16]
            lm17 = landmarks[17]
            lm18 = landmarks[18]
            lm19 = landmarks[19]
            lm20 = landmarks[20]


            thumb_raise=lm4.x > lm3.x
            index_raise=lm8.y < lm7.y
            middle_raise=lm12.y < lm11.y
            ring_raise=lm16.y < lm14.y
            pinky_raise=lm20.y < lm19.y



        hello = (thumb_raise and
                ring_raise and 
                pinky_raise and 
                index_raise and 
                middle_raise)
        
        hi = (not thumb_raise and
                not ring_raise and 
                not pinky_raise and 
                index_raise and 
                middle_raise)
            
        love = (
            thumb_raise and
            index_raise and
            not middle_raise and
            not ring_raise and
            pinky_raise)
            
        call = (
            lm8.x < lm7.x and
            lm12.x < lm11.x and
            lm16.x < lm15.x and
            lm4.y < lm3.y and
            lm20.x > lm18.x and
            lm20.y > lm0.y
        )

        like = (
            lm8.x < lm7.x and
            lm12.x < lm11.x and
            lm16.x < lm15.x and
            lm20.x < lm18.x and
            lm4.y < lm3.y and
            lm3.y < lm5.y
        )

        ok = (
            pinky_raise and
            ring_raise and
            middle_raise and
            lm8.y > lm6.y and
            lm4.x > lm2.x
        )

        sos = (
            not thumb_raise and
            lm8.y > lm4.y and
            lm12.y > lm4.y and
            lm16.y > lm4.y and
            lm20.y > lm4.y and 
            not lm20.y > lm0.y
        )
            
        if hello:
            output="hello !"
        elif love:
            output="love u"
        elif like:
            output="good"
        elif sos:
            output="SOS"
        elif call:
            output="calling"
        elif ok:
            output="Oke"
        else:
            output=""



    cv2.putText(image,output,(10,50),1,cv2.FONT_HERSHEY_COMPLEX,(255,0,0),2)
    cv2.imshow("Hand Tracking", image)

    if cv2.waitKey(5) & 0xFF == ord("c") or cv2.getWindowProperty("Hand Tracking", cv2.WND_PROP_VISIBLE) < 1 :
        break

    

cap.release()
cv2.destroyAllWindows()
