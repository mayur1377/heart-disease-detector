from pyexpat import model
import streamlit as st
import numpy as np
import pandas as pd
import sklearn
import pickle
from sklearn.metrics import classification_report
st.set_page_config(layout="wide")
st.markdown("""
<style>
.big-font {
    font-size:2rem !important;
    text-align:center;
    color:white;

}
.sizebig
{
    font-size:2.5rem;
    font-style:bold;
    
}
</style>
""", unsafe_allow_html=True)

st.sidebar.write('<p class="sizebig">MORE INFORMATION</p>', unsafe_allow_html=True)
st.sidebar.header("HOW TO KEEP YOUR HEART HEALTHY?")
st.sidebar.write("1. Don't smoke or use tobacco")
st.sidebar.write("2. Get moving: Aim for at least 30 to 60 minutes of activity daily")
st.sidebar.write("3. Eat a heart-healthy diet")
st.sidebar.write("4. Maintain a healthy weight")
st.sidebar.write("5. Get good quality sleep")
st.sidebar.write("6. Manage stress")
st.sidebar.write("7. Get regular health screenings")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("")
st.sidebar.write("DEVELOPED BY [MAYUR](https://github.com/mayur1377) ")


st.markdown('<p class="big-font">HEART DISEASE PREDICTOR</p>', unsafe_allow_html=True)
def userinput():
    age = st.number_input('ENTER YOUR AGE: ')
    sex  = st.selectbox('SEX',('MALE' ,  'FEMALE'))
    if sex=='MALE' : sex=1
    elif sex=='FEMALE': sex=0
    # st.write(sex)

    cp = st.selectbox('CHEST PAIN TYPE',('TYPICAL ANGINA','ATYPICAL ANGINA','NON-ANGINAL PAIN','ASYMPTOMATIC'))
    if(cp=='TYPICAL ANGINA'):cp=0
    elif cp=='ATYPICAL ANGINA':cp=1
    elif cp=='NON-ANGINAL PAIN' :cp=2
    else : cp=3

    
    tres = st.number_input('RESTING BLOOD PREASSURE in mm Hg: ')

    chol = st.number_input('SERUM CHOLESTORAL IN mg/dl: ')

    fbs = st.selectbox('FASTING BLOOD SUGAR >120 mg/dl ',('TRUE' , 'FALSE'))
    if(fbs=='TRUE') : fbs=1
    else : fbs=0

    res = st.number_input('RESTING ELECTROCARDIOGRAPHIC RESULTS: ')
    tha = st.number_input('MAXIMUM HEART RATE ACHIEVED: ')


    exa = st.selectbox('EXERCISE INDUCED ANGINA: ',('YES','NO'))
    if exa=='YES' : exa=1
    else : exa=0

    old = st.number_input('OLDPEAK ')
    slope = st.number_input('HE SLOPE OF THE PEAK EXERCISE ST SEGMEN: ')
    ca = st.selectbox('NUMBER OF MAJOR VESSELS COLORED BY FLOUROSOPY',(0,1,2,3))

    thal = st.selectbox('THAL',('NORMAL','FIXED DEFECT','REVERSABLE DEFECT'))
    if thal=='NORMAL': thal=0
    elif thal=="FIXED DEFECT":thal=1
    else :thal=4
    # st.write(thal)


    data = {'age': age,
            'sex': sex, 
            'cp': cp,
            'trestbps':tres,
            'chol': chol,
            'fbs': fbs,
            'restecg': res,
            'thalach':tha,
            'exang':exa,
            'oldpeak':old,
            'slope':slope,
            'ca':ca,
            'thal':thal
            }
    features = pd.DataFrame(data, index=[0])
    return features
input_df = userinput()

#load the dataset
heartdata=pd.read_csv('heart_disease_data.csv')
#drop the target from heartdata
heartdata=heartdata.drop(columns=['target'])
#concat the user value to heartdata first row
df=pd.concat([input_df , heartdata], axis=0)
#only user data is there in df
df = df[:1] # Selects only the first row (the user input data)


# load the model
model = pickle.load(open('modle.pkl', 'rb'))

# Apply model to make predictions
prediction = model.predict(df)

# st.subheader('Prediction')
# st.write(prediction)
# if prediction==1: prediction="Looks like your heart isint in a healthy condition , check the doctors now"
# elif prediction==0 : prediction="you are good to go"
form = st.form(key='my-form')
submit = form.form_submit_button('SUBMIT')
if submit:
    if prediction==0 : st.write("EVERYTHING SEEMS HEALTHY! HAVE A GREAT DAY")
    else  : st.write("YOUR HEART DOSENT SEEM HEALTHY , VISIT A [CARDIOLIGIST](https://www.google.com/search?q=cardiologist+near+me&rlz=1C1RXQR_enIN1028IN1028&oq=CARDIO&aqs=chrome.0.69i59j69i57j0i433i512l2j0i131i433i512l2j0i402j69i60.1824j0j7&sourceid=chrome&ie=UTF-8) NOW")


