# [HEART DISEASE DETECTOR](https://heart-disease-detector.streamlitapp.com/)

This is a web based machine learning project which is used to check if a patient is suffering from a heart disease or not by taking the parameters from the user

## PROBLEM
Cardiovascular disease is the leading cause of deaths in India both across the rural and urban population, according to the World Atlas. This is backed up by data from the Centers for Disease Control and Prevention, which identifies heart disease, chronic obstructive pulmonary disease and stroke as the top three killers.

Cardiovascular diseases accounts for 24.8% of deaths in India, the early prognosis of cardiovascular diseases can aid in making decisions on lifestyle changes in high risk patients and in turn reduce the complications.

This project focuses to reduce the risk factor by letting a patient know if their heart is at a risk or not.

## SOLUTION

in this I've trained the **Logistic Regression Model** to check if a patient is at a risk of a heart disease


## DATASET
I've used a data set from [kaggle](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset) which contains a record of a total of 304 patients.

You can [view](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset) the file directly here.
 
 The data contains **303** readings with **0** null values.
 
 The accuracy of the trained model is : **88.01%** .
 
## The dataset contains the following values
-   Age : Age of the patient
    
-   Sex : Sex of the patient
    
-   exang: exercise induced angina (1 = yes; 0 = no)
    
-   ca: number of major vessels (0-3)
    
-   cp : Chest Pain type chest pain type
    
    -   Value 1: typical angina
    -   Value 2: atypical angina
    -   Value 3: non-anginal pain
    -   Value 4: asymptomatic
-   trtbps : resting blood pressure (in mm Hg)
    
-   chol : cholestoral in mg/dl fetched via BMI sensor
    
-   fbs : (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
    
-   rest_ecg : resting electrocardiographic results
    
    -   Value 0: normal
    -   Value 1: having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)
    -   Value 2: showing probable or definite left ventricular hypertrophy by Estes' criteria
-   thalach : maximum heart rate achieved
    
-   target : 0= less chance of heart attack 1= more chance of heart attack


##  LIBRARIES USED
PANDAS
NUMPY
STREAMLIT
SKLEARN

## HOSTING
the project is deployed with [streamlit](https://streamlit.io/) , you can check the live demo [here](https://heart-disease-detector.streamlitapp.com/)

# RESULT
the poject has been sucessfully implemented with an accuracy of  **88.01%**
CHECK OUT THE LIVE [PROJECT](https://heart-disease-detector.streamlitapp.com/)
