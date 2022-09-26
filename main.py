
from pickle import FALSE
import cv2
import numpy as np
import os
import face_recognition
from datetime import datetime
import speech_recognition as sr
import pyttsx3
import win32api
import random
import pythoncom
from flask import Flask, render_template,request
pythoncom.CoInitialize()
app=Flask(__name__)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

def fa():
    i=0
    path = 'ImagesAttendance'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
        print(classNames)
    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList
    def markAttendance(name):
        with open('Attendance.csv','r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split('\n')
                nameList.append(entry[0])
                if name not in nameList:
                    now = datetime.now()
                    dtString = now.strftime('%H:%M:%S')
                    f.writelines(f'{name},{dtString}'+'\n')
                 
                    break
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#img = captureScreen()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
 
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
        if not facesCurFrame:
                    for (x, y, w, h) in faces:
                         cv2.rectangle(img, (x, y), (x+w,y+h), (0, 255, 0), 2)
                         cv2.putText(img, "Not found", (x - 10, y - 10), cv2.FONT_ITALIC, 1, (0, 0, 255), 3)
                         win32api.Beep(500,100)                 

        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
#print(faceDis)
            matchIndex = np.argmin(faceDis)
 
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                
            
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            
            def talk(text):
                engine.say(text)
                engine.runAndWait()
        
            markAttendance(name)
            
            talk("HELLO  ")
            talk(name)
          
        cv2.imshow('Webcam',img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break    
        
    cap.release()
    cv2.destroyAllWindows()
def ta():
    
    i=0
    path = 'criminal'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
        print(classNames)
    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList
    def markAttendance(name):
        with open('Attendance.csv','r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split('\n')
                nameList.append(entry[0])
                if name not in nameList:
                    now = datetime.now()
                    dtString = now.strftime('%H:%M:%S')
                    f.writelines(f'{name},{dtString}'+'\n')
                    break
   
    encodeListKnown = findEncodings(images)
    print('Encoding Complete')
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
#img = captureScreen()
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
 
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
 
        for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
#print(faceDis)
            matchIndex = np.argmin(faceDis)
 
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                
#print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,0,255),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            cv2.putText(img, "CRIMINAL...BEWARE!!", (30, 30), cv2.FONT_ITALIC, 1, (0, 0, 255), 3)
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            engine.setProperty('voice', voices[0].id)
            
            def talk(text):
                engine.say(text)
                engine.runAndWait()
            talk("Criminal beware")
            talk(name)
            win32api.Beep(750,3000) 
        
            if i==0:
                markAttendance(name)
                
                
            i=i+1
        cv2.imshow('Webcam',img)
        
            
        
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()           
       


@app.route("/",methods=['GET','POST'])
def home():   
    return render_template("index.html")
@app.route("/p",methods=['GET','POST'])
def tt():
    if request.method=="POST" and 'numb' in request.form:
        
        a=request.form.get('numb')
        if(a=="1"):
            print("1")
            fa()
        if(a=="2"):
            ta()
       
    return render_template("index.html")
app.run()