# [HEART DISEASE DETECTOR](https://heart-disease-detector.streamlitapp.com/)

This is a web based machine learning project which is used to check if a patient is suffering from a heart disease or not by taking the parameters from the user

# PROBLEM
Cardiovascular disease is the leading cause of deaths in India both across the rural and urban population, according to the World Atlas. This is backed up by data from the Centers for Disease Control and Prevention, which identifies heart disease, chronic obstructive pulmonary disease and stroke as the top three killers.

Cardiovascular diseases accounts for 24.8% of deaths in India, the early prognosis of cardiovascular diseases can aid in making decisions on lifestyle changes in high risk patients and in turn reduce the complications.

This project focuses to reduce the risk factor by letting a patient know if their heart is at a risk or not.

# SOLUTION

in this I've trained the **Logistic Regression Model** to check if a patient is at a risk of a heart disease


# SETUP

To install the dependencies, you can simply follow this steps.

Clone the project repository:
```bash
git clone https://github.com/mayur1377/heart-disease-detector
cd heart-disease-detector
```

To create and activate the virtual environment, follow these steps:



**Using `virtualenv`**

```bash

$ virtualenv streamlit --python=python3

# Activate the virtual environment:
$ source heart-disease-detector/bin/activate

# To deactivate (when you're done):
(heart-disease-detector)$ deactivate
```

To install the requirements using `pip`, once the virtual environment is active:
```bash
(heart-disease-detector)$ pip install -r requirements.txt
```

#### Running the script

Finally, if you want to run the main script:
```bash
(heart-disease-detector)$ streamlit run HEARTDISEASEDETECTOR.py
```

# DATASET
I've used a data set from [kaggle](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset) which contains a record of a total of 304 patients.

You can [view](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset) the file directly here.
 
 The data contains **303** readings with **0** null values.
 
 The accuracy of the trained model is : **88.01%** .
 
## The dataset contains the following values
- age
- sex
- chest pain type (4 values)
- resting blood pressure
- serum cholestoral in mg/dl
- fasting blood sugar > 120 mg/dl
- resting electrocardiographic results (values 0,1,2)
- maximum heart rate achieved
- exercise induced angina
- oldpeak = ST depression induced by exercise relative to rest
- the slope of the peak exercise ST segment
- number of major vessels (0-3) colored by flourosopy
- thal: 0 = normal; 1 = fixed defect; 2 = reversable defect


#  LIBRARIES USED
- pandas
- numpy
- streamlit
- sklearn

# HOSTING
The project is deployed with [streamlit](https://streamlit.io/) , you can check the live demo [here](https://heart-disease-detector.streamlitapp.com/)

# RESULT
The project has been sucessfully implemented with an accuracy of  **88.01%**
CHECK OUT THE LIVE [PROJECT](https://heart-disease-detector.streamlitapp.com/)
