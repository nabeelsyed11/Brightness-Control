# Importing Libraries
import cv2
import mediapipe as mp
from math import hypot
import screen_brightness_control as sbc
import numpy as np

# Initializing the Model
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
    max_num_hands=2
)

Draw = mp.solutions.drawing_utils

# Start capturing video from webcam
cap = cv2.VideoCapture(0)

while True:
    # Read video frame by frame
    success, frame = cap.read()
    if not success:
        break

    # Flip image
    frame = cv2.flip(frame, 1)

    # Convert BGR image to RGB image
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the RGB image
    Process = hands.process(frameRGB)

    landmarkList = []
    # if hands are present in image(frame)
    if Process.multi_hand_landmarks:
       # detect handmarks
       for handlm in Process.multi_hand_landmarks:
          for _id, landmarks in enumerate(handlm.landmark):
             # store height and width of image
             height, width, color_channels = frame.shape

             # calculate and append x, y coordinates
             # of handmarks from image(frame) to lmList
             x, y = int(landmarks.x * width), int(landmarks.y * height)
             landmarkList.append([_id, x, y])

          # draw Landmarks
          Draw.draw_landmarks(frame, handlm,
                         mpHands.HAND_CONNECTIONS)

    # If landmarks list is not empty
    if landmarkList:
       # store x,y coordinates of (tip of) thumb
       x_1, y_1 = landmarkList[4][1], landmarkList[4][2]

       # store x,y coordinates of (tip of) index finger
       x_2, y_2 = landmarkList[8][1], landmarkList[8][2]

       # draw circle on thumb and index finger tip
       cv2.circle(frame, (x_1, y_1), 7, (0, 255, 0), cv2.FILLED)
       cv2.circle(frame, (x_2, y_2), 7, (0, 255, 0), cv2.FILLED)

       # draw line from tip of thumb to tip of index finger
       cv2.line(frame, (x_1, y_1), (x_2, y_2), (249, 207, 221), 3)

       # calculate square root of the sum of
       # squares of the specified arguments.
       L = hypot(x_2 - x_1, y_2 - y_1)

       # Convert the distance to a brightness level
       brightness = np.interp(L, [30, 350], [0, 100])

       # Set screen brightness
       sbc.set_brightness(int(brightness))

       # Display the brightness level on the screen
       cv2.putText(frame, f'Brightness: {int(brightness)}%', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Display the frame
    cv2.imshow('Hand Tracking', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()