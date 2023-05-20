
# Personality-Prediction-via-CV
A system that predict the personality of a person with OCEAN values and resume.

## Objectives
This system can be used in many business parts/areas that may require expert candidates. This system will reduce the workload of the (workers in general/hiring, training, and firing department). This system will help the (related to workers in general) to select the right candidate for the desired job profile, which in turn provide the expert (all the workers in a company or country) for the organization. Admin can easily shortlist a candidate based on their personality scores and select the appropriate candidate for a particular job profile.
Using **Natural Language Processing (NLP)** can be defined as a process that enables a machine to become more like a human, because of this deeply cutting the distance between machines and humans. This system will focus not only on qualification and inexperience but also focuses on other important aspects, which are needed/demanded for a particular job position. Admin can store the data in excel sheet for further comparison and sorting of data.

## Background of Personality Perception
The ***Big Five Personality Traits*** model is based on findings from several independent researchers, and it dates back to the late 1950s. But the model as we know it now began to take shape in the 1990s.
Lewis Goldberg, a researcher at the Oregon Research Institute, is credited with naming the model "*The Big Five*." It is now considered to be an accurate and respected personality scale, which is routinely used by businesses and in psychological research.
The Big Five Personality Traits Model measures five key dimensions of people's personalities:

#Open to Experience: It involves various dimensions, like imagination, sensitivity, attentiveness, preference to variety, and curiosity.  
#Conscientiousness: This trait is used to describe the carefulness and diligence of the person. It is the quality that describes how organized and efficient a person is.
#Extraversion: It is the trait that describes how the best candidates can interact with people that is how good are his/her social skills.
#Agreeableness: It is a quality that analyses the individual behavior based on the generosity, sympathy, cooperativeness and ability to adjust with people.  
#Neuroticism: This trait usually describes a person to have mood swings and has extreme expressive power.
 

## Dependencies of System

-  os
- pandas
- numpy
- tkinter
- functools
- pyresparser
- sklearn
- nltk
- scaPy


## Description
The system built in this project predicts personality of peoples by using their gender, age, score of openness, conscientiousness, extraversion, agreeableness, neuroticism and experience. It parses all the data from CV/resume and on the result page, it shows all the information from the entered data and uploaded resume. This system uses logistic regression for training the model and pyresparser module for parsing the information from resume which is built using nltk and spaCy module in python.
Description of Methods and Flow in the System:

- ### train_model class 

>It contains two method which train the model and predict the result by giving the various values.
train method: It read the dataset for training the model from a csv file and build a model using Logistic Regression. It uses different 7 values for training the model.
test method: It predict the personality of a person by passing an array of values that contains gender, age and other 5 personality characteristics.

- ### main method

>We start with creating an object of train_model class and train the model by calling train method of class. Then we initialize a variable with Tk object and design the landing page of system using labels and button. A button with name Predict Personality is designed which calls predict_person¬ method. 


- ### predict_person method
> We withdraw the root tkinter window and create a new toplevel window and configure its size and attributes. We label the heading of window followed by various labels and their entries. For selecting of a resume file, user needs to press choose file button which then calls Openfile method that takes an argument of button. In predict_person method, various entries are taken for predicting the personality. Submit button pass all the values to prediction_result.

- ### OpenFile method
>It tries to open the directory with default address name and file types and except if file not chosen. After try except block, the method changes the name of choose file button in predict_person method with the base name of file so that user can know about the chosen file.
 
- ### prediction_result method 
>This method firstly closes the previous tkinter window which was used to take the data from user. After this, it calls test method of model object and stores the result returned by method. After this it parse all the information from resume and stores in a variable followed by a try except block which try to delete name and validate mobile number from fetched information from resume. Then it prints all the data submitted by user on console. After this, the method popup a full screen window which shows all the parsed information and predicted personality on GUI window along with the definition of each personality characteristic’s definition.

- ### check_type method

>It converts various strings and numbers into desired format and converts lists and tuples in string. 


