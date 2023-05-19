#from tkinter import Menu
import requests
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu

#For detection
import cv2
import os
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from pygame import mixer
from keras.models import model_from_json
from tensorflow.keras.utils import img_to_array
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, RTCConfiguration, VideoProcessorBase, WebRtcMode
import av

st.set_page_config(page_title='Driver Drowsiness Detection',page_icon=':oncoming_taxi:',layout='wide')

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("C:/Users/user/New folder/Styles/styles.css")

selected = option_menu(
        menu_title=None,  
        options=["Home", "Methodology", "Trial","Contact"],  
        icons=["house", "book","webcam", "envelope"],  
        menu_icon="cast",  
        default_index=0,  
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color":"#000000	"},
            "icon": {"color": "white", "font-size": "15px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "#28282b",
            },
            "nav-link-selected": {"background-color": "	#272536"},
        },
    )
#return selected

st.markdown(""" <style> .font {
font-size:17px ; font-family: 'Arial'; color: #FFFFFF;} 
</style> """, unsafe_allow_html=True)

home_img = Image.open("C:/Users/user/New folder/Images/img4.jpg")

if selected == "Home":
    st.write('##')
    st.markdown("<h1 style='text-align: center; color: #9b9b9e;'>DRIVER DROWSINESS DETECTION</h1>", unsafe_allow_html=True)
    st.image(home_img)
    st.write("##")
    st.write("##")
    st.write("##")

    st.markdown('<p class="font">These days, we see people from various professions facing long nights at work, jobs that are fundamental to the well-being and comfort of the society. As a result, they are left with only one option, to get behind the wheel while feeling tired and sleepy. This is something most drivers would have gone through atleast once in their lives. However, this is incredibly dangerous.</p>', unsafe_allow_html=True)
    st.markdown("<p class ='font'>For some who find themselves getting drowsy, a brief state of unconsciousness, called a microsleep, may occur. In these instances, the driver might still even have their eyes open, but they are not in proper control of their vehicle. Exhaustion can be as bad as driving under the influence of alcohol. Research has shown that 24 hours of sleep deprivation causes the same level of impairment as someone whose blood alcohol (BAC) level is at 0.10 percent a number that’s over the legal limit.</p>", unsafe_allow_html=True)

    st.markdown("<p class ='font'>There are safeguards in place for those whose jobs rely on long periods of driving. For example, truck drivers are forbidden from driving past 14 hours after their shift starts. But for the average driver, there are no such safeguards. Drowsiness is a significant cause of accidents, with studies finding that loss of concentration is responsible for 25% of road accidents. Preventing drowsy drivers from getting behind the wheel is important. Being able to detect drowsy drivers and remind them to be safe and take a break if they’re feeling sleepy is one way to address this issue.</p>", unsafe_allow_html=True)

if selected == "Methodology":
    st.markdown("<h2 style=color: #9b9b9e;'>OBJECTIVE OF THE PROJECT </h2>", unsafe_allow_html=True)    

    st.markdown("<p class='font'>In this project, we are creating a drowsiness detection system using OpenCV and Keras that will detect if a person is drowsy dependent on if the person's eyes are open or closed for a particular time period. This system will alert the driver when drowsiness is detected.</p>", unsafe_allow_html=True)
    st.write('##')    
    st.markdown("<h2 style=color: #9b9b9e;'>PROCEDURE </h2>", unsafe_allow_html=True)    
    st.markdown("<p class='font'>1. Take image input from the webcam </p>", unsafe_allow_html=True)
    st.markdown("<p class='font'>2. Detect the face and eyes </p>", unsafe_allow_html=True)
    st.markdown("<p class='font'>3. Feed them to the classifier </p>", unsafe_allow_html=True)
    st.markdown("<p class='font'>4. Classifier will categorize whether the eyes are open or close </p>", unsafe_allow_html=True)
    st.markdown("<p class='font'>5. Calculate score to check if the person is drowsy </p>", unsafe_allow_html=True)
    st.markdown("<p class='font'>6. Alert the driver if score is greater than a particular value </p>", unsafe_allow_html=True)
    st.write('##')
    st.markdown("<h2 style=color: #9b9b9e;'>CONVOLUTIONAL NEURAL NETWORK (CNN) </h2>", unsafe_allow_html=True)    
    st.markdown("<p class='font'>A deep learning CNN model to built the classifier for detecting if the eyes are closed or open. </p>", unsafe_allow_html=True)
    st.markdown("<p class='font'>In deep learning, a convolutional neural network (CNN/ConvNet) is a class of deep neural networks, most commonly applied to analyze visual imagery. It performs extremely well for image classification. A deep learning CNN consists of three layers: a convolutional layer, a pooling layer and a fully connected (FC) layer. The convolutional layer is the first layer while the FC layer is the last. From the convolutional layer to the FC layer, the complexity of the CNN increases. It is this increasing complexity that allows the CNN to successively identify larger portions and more complex features of an image until it finally identifies the object in its entirety. </p>", unsafe_allow_html=True)
    st.markdown("<p class='font'>In this system, there are 3 convolutional layers and 1 fully connected layer. A Relu activation function is used in all the layers except the output layer in which I have used softmax </p>", unsafe_allow_html=True)
    st.markdown("<p class='font'>In order to detect the face and eyes of the driver, we use haar cascading. </p>", unsafe_allow_html=True)


if selected == "Trial":
    st.header("Webcam Live Feed")
    st.write("Select the run checkbox to use webcam and detect drowsiness")
    run = st.checkbox('Run')
    FRAME_WINDOW = st.image([])
    camera = cv2.VideoCapture(0)
    mixer.init()
    sound = mixer.Sound('alarm.wav')
    path = os.getcwd()
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    score = 0
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    left_eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_lefteye_2splits.xml')
    right_eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_righteye_2splits.xml')
    model =load_model('models/model.h5')

    while run:
        ret, frame = camera.read()
        height,width = frame.shape[0:2]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces= face_cascade.detectMultiScale(gray, scaleFactor= 1.2, minNeighbors=3)
        left_eye= left_eye_cascade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors=1)
        right_eye= right_eye_cascade.detectMultiScale(gray, scaleFactor= 1.1, minNeighbors=1)

        cv2.rectangle(frame, (0,height-50),(200,height),(0,0,0),thickness=cv2.FILLED)
        
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h), color= (255,255,255), thickness=1 )
            
        for (ex,ey,ew,eh) in right_eye:
            cv2.rectangle(frame,pt1=(ex,ey),pt2=(ex+ew,ey+eh), color= (255,255,255), thickness=1 )
            
            # preprocessing steps
            reye= frame[ey:ey+eh,ex:ex+ew]
            reye= cv2.resize(reye,(80,80))
            reye= reye/255
            reye= reye.reshape(80,80,3)
            reye= np.expand_dims(reye,axis=0)
            # preprocessing is done now model prediction
            rprediction = model.predict(reye)
            
            for (ex,ey,ew,eh) in left_eye:
                cv2.rectangle(frame,pt1=(ex,ey),pt2=(ex+ew,ey+eh), color= (255,255,255), thickness=1 )

                    # preprocessing steps
                leye= frame[ey:ey+eh,ex:ex+ew]
                leye= cv2.resize(leye,(80,80))
                leye= leye/255
                leye= leye.reshape(80,80,3)
                leye= np.expand_dims(leye,axis=0)
                    # preprocessing is done now model prediction
                lprediction = model.predict(leye)

                    # if eyes are closed
                if rprediction[0][0]>0.80 and lprediction[0][0]>0.80:
                    cv2.putText(frame,"Closed",(10,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
                    cv2.putText(frame,'Score:'+str(score),(100,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
                    score=score+1
                    if(score>8):
                        cv2.imwrite(os.path.join(path,'image.jpg'),frame)
                        try:
                            sound.play()
                        except:
                            pass

                else:
                    cv2.putText(frame,'Open',(10,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)  
                    cv2.putText(frame,'Score:'+str(score),(100,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
                    score = score-1
                    if (score<0):
                        score=0

        FRAME_WINDOW.image(frame, channels='BGR')
    else:
        st.write('Stopped')

    

if selected == "Contact":
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")
        contact_form = """
        <form action="https://formsubmit.co/aryachandran1999@gmail.com" method="POST">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your e-mail ID" required>
            <textarea name="message" placeholder="Your message" required></textarea>
            <button type="submit">Send</button>
        </form>
        """

        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()

            

    
    
