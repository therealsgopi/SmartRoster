# SMART ROSTER: An Automated Face Recognition System

## Description 
Taking attendance has long been a manual task that is performed by the person responsible for conducting the session. This is oftentimes a slow and lengthy process, taking up time which could be used for teaching. This led us to create this project which will use face recognition to mark attendance, with the only hardware being used is a smartphone camera.

## Module-wise Description
For the backend portion of our project, we have set up our face recognition system using the face_recognition python library, that is built on top of dlib, a face recognition system made using deep learning techniques. This is our primary tool and will be used for extracting all the faces present in the class image and then compare the encodings of the extracted images with our database to find matches. Open CV is also used to process and change the encoding of our extracted face images so that they can be used with face_recognition.

In terms of frontend, we have used Django to create a framework that will be used to upload our images to the server and then allow us to display and download the attendance list that is returned by the backend. We plan to expnad it further to make it more robust.

The only hardware that we need is our smartphone's camera which will be used to take the class photo.

## Requirements
- python <= 3.8.0
- face_recognition
- dlib python package
- Open CV
- Django python framework - for backend
- React.js library - for frontend
- Tensorflow

## How to run
### Front-end
1) Clone the repository and navigate to the *frontend* directory.
2) Run `npm i` to download all the requirements for the react frontend.
3) Run the command `npm run start` in the same directory to get the frontend running.
4) Next naviagte to the *server* directory.
5) Run `pip install -r requirements.txt` to download all the requirements for the django server.
6) Run the command `py manage.py runserver` in the same directory to get the backend running.
7) Go to http://localhost:3000/ to access the Attendance Portal.
8) Upload a class image, and the students register number and status (present/absent) will be returned from the backend after applying our proposed model.
9) You may download the attendance report using the 'Download Attendance Report' button.
     
### Python Notebooks
1) Clone the repository and navigate to the python notebook of the approach you wish to run.
2) Open the notebook using Google Colab or Jupyter Notebook or run the file locally ensuring you have installed the requirements mentioned above.
3) You may either link your google drive to provide images for training and testing or upload locally in the session of the python notebook.
4) Run cell wise to first generate the embeddings for the train images and then run it on the test image to identify and classify the segmented face.
     
> **_NOTE:_**  Run the Python Notebooks in a GPU-powered environment/system. 
