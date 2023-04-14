from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .serializers import ImageSerializer
from .models import class_image

import mtcnn
import face_recognition
import numpy as np
import cv2
import os

# additional libraries
import numpy as np

def img_resize(path):
  img = cv2.imread(path)
  (h, w) = img.shape[:2]
  width = 1000
  ratio = width / float(w)
  height = int(h * ratio)
  #resizing the image with custom width and height
  return cv2.resize(img, (width, height))


def mark_attendance_status(train_face_names, face_names_recog):
  attendance_status = []
  for stud in train_face_names:
    if stud in face_names_recog:
      attendance_status.append('PRESENT')
    else:
      attendance_status.append('ABSENT')
  return attendance_status

# Create your views here.

@csrf_exempt 
def index(request):
    print("Server started at http://127.0.0.1:8000/")
    return HttpResponse("Server started at http://127.0.0.1:8000/")

@csrf_exempt
@api_view(['POST'])
def mark_attendance(request):
    #list to store the training face encodings
    train_face_encs = []
    #list to store the training names of person
    train_face_names = []

    #Training the model
    training_images = r'C:\Users\yashs\Documents\D-Drive\Sem 6\TARP\Attendance-Portal\server\mark_attendance\TrainImages'
    for file in os.listdir(training_images):
        img = img_resize(training_images + '/' + file)
        # img = face_recognition.load_image_file(training_images + '/' + file)
        # img = cv2.imread(training_images + '/' + file)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_enc = face_recognition.face_encodings(img)[0]
        train_face_encs.append(face_enc)
        train_face_names.append(file.split('.')[0])

    #Testing the model
    testing_images = r'C:\Users\yashs\Documents\D-Drive\Sem 6\TARP\Attendance-Portal\server\mark_attendance\ClassImages'
    for file in os.listdir(testing_images):
        img = img_resize(testing_images + '/' + file)
        # img = face_recognition.load_image_file(testing_images + '/' + file)
        # img = cv2.imread(testing_images + '/' + file)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # face_loc = face_recognition.face_locations(img)
        face_locs = face_recognition.face_locations(img, model = "cnn")
        face_encs = face_recognition.face_encodings(img, face_locs)
        
        face_names_recog = []
        for face_enc in face_encs:
            face_matches = face_recognition.compare_faces(train_face_encs, face_enc)
            face_distances = face_recognition.face_distance(train_face_encs, face_enc)
            best_match_index = np.argmin(face_distances)
            face_name_recog = "unknown"
            # print(face_matches)
            # print(face_distances)
            # print(train_face_names[best_match_index])
            if face_matches[best_match_index]:
                face_name_recog = train_face_names[best_match_index]
            face_names_recog.append(face_name_recog)
    
        for (top, right, bottom, left), face_name in zip(face_locs, face_names_recog):
            cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 3)
            cv2.putText(img, face_name, (left+2, bottom+20), cv2. FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
        # cv2.imshow(img)
        attendance_status = mark_attendance_status(train_face_names, face_names_recog)
        print(train_face_names)
        print("*"*50)
        print(face_names_recog)

    # Mock data for testing purpose
    # return JsonResponse({"regno": ['20BCE1720', '20BAI1546', '20BCE1251', '20BCE1109', '20BCE1908', '20BCE1653', '20BCE1871', '20BCE1806', '20BCE1170', '20BCE1848', '20BCE1789', '20BCE1102', '20BCE1886', '20BCE1723', '20BCE1098', '20BCE1318'],
    #                      "status":  ['PRESENT', 'ABSENT', 'PRESENT', 'PRESENT', 'ABSENT', 'PRESENT', 'PRESENT', 'PRESENT', 'PRESENT', 'PRESENT', 'PRESENT', 'PRESENT', 'PRESENT', 'ABSENT', 'PRESENT', 'ABSENT', 'PRESENT', 'PRESENT', 'PRESENT', 'PRESENT']})
    return JsonResponse({"regno": train_face_names,
                            "status":  attendance_status})