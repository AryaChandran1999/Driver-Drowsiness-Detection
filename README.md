# DRIVER-DROWSINESS-DETECTION

Driver drowsiness technology is a safety technology to prevent car
accidents caused by drivers who fall asleep while driving. 

## OBJECTIVE
The objective of this Python project is to build a drowsiness
detection system that will detect if a driver is drowsy depending
on if the person’s eyes are closed for a particular time period . This
system will alert the driver when drowsiness is detected.

## DATA
The data is the 'yawn_eye_dataset_new' obtained from Kaggle which comprises of 2900 images of people's eyes under different lighting conditions.
Link : https://www.kaggle.com/datasets/serenaraju/yawn-eye-dataset-new

## METHODOLOGY
The project is entirely done using python at the front and back end. 

### Front-end :
The frontend is done using streamlit, which is a very easy way of creating a user interface. UI is a multipage webapp which has four tabs:
1. HOME - which gives an introduction to the topic
2. METHODOLOGY - which talks about the steps involved in the detection system
3. TRIAL - where you can test the detection system which takes input from your webcam
4. CONTACT - in case of any queries related to the project, you can send me an e-mail

All the front-end related files can be found in the UI folder.

### Back-end :
In the back-end, I have created a deep learning CNN model to classify if the person's eyes are closed or open. CNN performs very well with image classification. In this system, there are 3 convolutional layers and 1 fully connected layer. A Relu activation function is used in all the layers except the output layer in which I have used softmax. The model gave an accuracy of 80%.
The final_model file is the model used. 

In order to build the detection system, I have used OpenCV and haar cascading to detect the driver's face and eyes. 

### Step-by-step Procedure:
1. Take image input from the webcam
2. Detect the face and eyes
3. Feed them to the classifier
4. Classifier will categorize whether the eyes are open or close
5. Calculate score to check if the person is drowsy
6. Alert the driver if score is greater than a particular value

final_detection file is the driver drowsiness detection system. alarm.wav is the sound that is played when the driver is detected as drowsy.
