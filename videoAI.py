##importing libraries - not reinventing the wheel
from tkinter import *
import mediapipe as mp
import numpy as np
import random
import time
import cv2

tk = Tk()
tk.state('zoomed')

WIDTH = tk.winfo_screenwidth()
HEIGHT = tk.winfo_screenheight()

canvas = Canvas(tk, width = WIDTH, height = HEIGHT)
canvas.configure(bg='black')
tk.title("arhsim")
canvas.pack()

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture('astro.mp4')

with mp_pose.Pose(
  min_detection_confidence=0.5,
  min_tracking_confidence=0.5) as pose:

  while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    image = cv2.cvtColor(cv2.flip(frame, 1), cv2.COLOR_BGR2RGB)
    image.flags.writeable = False

    results = pose.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    try:
      landmarks = results.pose_landmarks.landmark

      NOSE= [WIDTH * landmarks[mp_pose.PoseLandmark.NOSE.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.NOSE.value].y]

      LEFT_EYE_INNER= [WIDTH * landmarks[mp_pose.PoseLandmark.LEFT_EYE_INNER.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.LEFT_EYE_INNER.value].y]
      LEFT_EYE= [WIDTH * landmarks[mp_pose.PoseLandmark.LEFT_EYE.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.LEFT_EYE.value].y]
      LEFT_EYE_OUTER= [WIDTH * landmarks[mp_pose.PoseLandmark.LEFT_EYE_OUTER.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.LEFT_EYE_OUTER.value].y]
      LEFT_EAR= [WIDTH * landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.LEFT_EAR.value].y]
      MOUTH_LEFT= [WIDTH * landmarks[mp_pose.PoseLandmark.MOUTH_LEFT.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.MOUTH_LEFT.value].y]
      LEFT_SHOULDER= [WIDTH * landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
      LEFT_ELBOW= [WIDTH * landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
      LEFT_WRIST= [WIDTH * landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
      LEFT_PINKY= [WIDTH * landmarks[mp_pose.PoseLandmark.LEFT_PINKY.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.LEFT_PINKY.value].y]
      LEFT_INDEX= [WIDTH * landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.LEFT_INDEX.value].y]
      LEFT_THUMB= [WIDTH * landmarks[mp_pose.PoseLandmark.LEFT_THUMB.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.LEFT_THUMB.value].y]
      LEFT_HIP= [WIDTH * landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
      LEFT_KNEE= [WIDTH * landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
      LEFT_ANKLE= [WIDTH * landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
      LEFT_HEEL= [WIDTH * landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.LEFT_HEEL.value].y]
      LEFT_FOOT_INDEX= [WIDTH * landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y]

      RIGHT_EYE_INNER= [WIDTH * landmarks[mp_pose.PoseLandmark.RIGHT_EYE_INNER.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.RIGHT_EYE_INNER.value].y]
      RIGHT_EYE= [WIDTH * landmarks[mp_pose.PoseLandmark.RIGHT_EYE.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.RIGHT_EYE.value].y]
      RIGHT_EYE_OUTER= [WIDTH * landmarks[mp_pose.PoseLandmark.RIGHT_EYE_OUTER.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.RIGHT_EYE_OUTER.value].y]
      RIGHT_EAR= [WIDTH * landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.RIGHT_EAR.value].y]
      MOUTH_RIGHT= [WIDTH * landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.MOUTH_RIGHT.value].y]
      RIGHT_SHOULDER= [WIDTH * landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
      RIGHT_ELBOW= [WIDTH * landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
      RIGHT_WRIST= [WIDTH * landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
      RIGHT_PINKY= [WIDTH * landmarks[mp_pose.PoseLandmark.RIGHT_PINKY.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.RIGHT_PINKY.value].y]
      RIGHT_INDEX= [WIDTH * landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.RIGHT_INDEX.value].y]
      RIGHT_THUMB= [WIDTH * landmarks[mp_pose.PoseLandmark.RIGHT_THUMB.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.RIGHT_THUMB.value].y]
      RIGHT_HIP= [WIDTH * landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.RIGHT_HIP.value].y]
      RIGHT_KNEE= [WIDTH * landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.RIGHT_KNEE.value].y]
      RIGHT_ANKLE= [WIDTH * landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE.value].y]
      RIGHT_HEEL= [WIDTH * landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.RIGHT_HEEL.value].y]
      RIGHT_FOOT_INDEX= [WIDTH * landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].x, HEIGHT * landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].y]

    except Exception as e:
      #print(f'--error occured--\t\t{e}')
      continue

    mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    filename = PhotoImage(file = "bc.png")
    canvas.create_image(NOSE[0], NOSE[1], anchor=CENTER, image=filename)

    canvas.create_polygon([LEFT_SHOULDER[0],LEFT_SHOULDER[1],RIGHT_SHOULDER[0],RIGHT_SHOULDER[1],RIGHT_HIP[0],RIGHT_HIP[1],LEFT_HIP[0],LEFT_HIP[1]],outline='gray', fill='chartreuse4', width=3)

##    canvas.create_line(MOUTH_LEFT[0], MOUTH_LEFT[1], LEFT_SHOULDER[0], LEFT_SHOULDER[1], fill='gray', width=2)
##    canvas.create_line(MOUTH_RIGHT[0], MOUTH_RIGHT[1], RIGHT_SHOULDER[0], RIGHT_SHOULDER[1], fill='gray', width=2)

    canvas.create_line(LEFT_SHOULDER[0], LEFT_SHOULDER[1], LEFT_ELBOW[0], LEFT_ELBOW[1], fill='green', width=14)
    canvas.create_line(RIGHT_SHOULDER[0], RIGHT_SHOULDER[1], RIGHT_ELBOW[0], RIGHT_ELBOW[1], fill='green', width=14)

    canvas.create_line(LEFT_ELBOW[0], LEFT_ELBOW[1], LEFT_INDEX[0], LEFT_INDEX[1], fill='green', width=12)
    canvas.create_line(RIGHT_ELBOW[0], RIGHT_ELBOW[1], RIGHT_INDEX[0], RIGHT_INDEX[1], fill='green', width=12)

    canvas.create_oval(LEFT_INDEX[0]-25, LEFT_INDEX[1]-25, LEFT_INDEX[0]+25, LEFT_INDEX[1]+25, fill = "white")
    canvas.create_oval(RIGHT_INDEX[0]-25, RIGHT_INDEX[1]-25, RIGHT_INDEX[0]+25, RIGHT_INDEX[1]+25, fill = "white")

    canvas.create_line(LEFT_HIP[0], LEFT_HIP[1], LEFT_KNEE[0], LEFT_KNEE[1], fill='gray', width=26)
    canvas.create_line(RIGHT_HIP[0], RIGHT_HIP[1], RIGHT_KNEE[0], RIGHT_KNEE[1], fill='gray', width=26)

    canvas.create_line(LEFT_KNEE[0], LEFT_KNEE[1], LEFT_HEEL[0], LEFT_HEEL[1], fill='dark olive green', width=14)
    canvas.create_line(RIGHT_KNEE[0], RIGHT_KNEE[1], RIGHT_HEEL[0], RIGHT_HEEL[1], fill='dark olive green', width=14)

    canvas.create_oval(LEFT_HEEL[0]-25, LEFT_HEEL[1]-25, LEFT_HEEL[0]+25, LEFT_HEEL[1]+25, fill = "white")
    canvas.create_oval(RIGHT_HEEL[0]-25, RIGHT_HEEL[1]-25, RIGHT_HEEL[0]+25, RIGHT_HEEL[1]+25, fill = "white")

    tk.update()
    #time.sleep(0.001)
    canvas.delete('all')

    cv2.imshow('arhsim', image)

    if cv2.waitKey(25) & 0xFF == 27:
      break

  canvas.mainloop()
  cap.release()
  cv2.destroyAllWindows()
