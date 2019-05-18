# Emotion Recognition with Convolutional Neural Networks

##### With the recent advancements in facial recognition technology, we were interested in learning about how this process works and what are some ways computers can accurately represent emotions based on images.

##### Our data source was the following repository:
##### https://github.com/muxspace/facial_expressions
##### This repository contained thousands jpg files,each labled in a csv file with the emotion seen on each face. The images were labelled by graduate students in the program and the user id Column in the data set corresponded with the student who labelled it. 

<img src="https://github.com/schehrbanokhan/emotion_recognition_neural_network/blob/master/readme_image/data.jpg" width="300">

##### The data set contained 8 different emotion labels. We cleaned up the data set to get four common labels i.e. Happiness, Sadness, Anger and Neutral. We used over 12000 labelled images from this data source and changed their orientations to create a large data set of over 76000 images and ran them through our CNN to train it to identify emotions correctly. 

##### The CNN had 222,702 params and I trained it for 14 epochs. Each Epoch took about 45 minutes to run so this was no small undertaking. 

##### We collected the accuracy and loss from the train and test set. The graph below shows how the values change over time
<img src="https://github.com/schehrbanokhan/emotion_recognition_neural_network/blob/master/readme_image/AllAcc_AllLos.PNG" width="700">

## Results:
##### Our model is able to predict happiness and neutral facial expressions fairly well but fails at detecting facial expressions corresponding to sadness and anger.

##### Some example results are seen below:

<img src="https://github.com/schehrbanokhan/emotion_recognition_neural_network/blob/master/readme_image/1.jpg" height="200">
<img src="https://github.com/schehrbanokhan/emotion_recognition_neural_network/blob/master/readme_image/3.jpg" height="200">
<img src="https://github.com/schehrbanokhan/emotion_recognition_neural_network/blob/master/readme_image/4.jpg" height="200">
<img src="https://github.com/schehrbanokhan/emotion_recognition_neural_network/blob/master/readme_image/5.jpg" height="200">
<img src="https://github.com/schehrbanokhan/emotion_recognition_neural_network/blob/master/readme_image/7.jpg" height="200">
<img src="https://github.com/schehrbanokhan/emotion_recognition_neural_network/blob/master/readme_image/8.jpg" height="200">

##### The model predicts :
#####    - Neutral images as neutral 96% of the time
#####    - Happy images as happy 78% of the time
#####    - Anger images as NEUTRAL 83% of the time
#####    - Sadness images as NEUTRAL 86% of the time

##### This can be seen in the Confusion Matrix below

<img src="https://github.com/schehrbanokhan/emotion_recognition_neural_network/blob/master/readme_image/ConfusionMatrix.PNG" width="400">

## Possible improvements

##### The data set we used had a significantly larger set of images for happiness and neutral than sadness and anger. This means that the model was trained much better to recognize the neutral and happiness emotions.
##### In future creating a large data set with the same number of labels for each image may prove to be a useful tactic to improve performance and recognition.

##### Looking within the data set I was able to find some images that, I feel were labelled incorrectly. Facial expression recognition inherently is effected by social ques. Some faces that I percieved to be incorrectly labelled could be seen differently by another observer. This inherent bias in the data set could be removed by showing an image to a large, diverse set of people and chosing the most common label to associate with the expression. This tactic could have help improve the model accuracy, however this is a very time consuming process.  
