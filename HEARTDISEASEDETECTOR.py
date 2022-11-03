from pyexpat import model
import streamlit as st
import numpy as np
import pandas as pd
import pickle
st.set_page_config(layout="wide")
st.markdown("""
<style>
.big-font {
    font-size:2rem !important;
    text-align:center;
    color:color;

}
.sizebig
{
    font-size:2.5rem;
    font-style:bold;   
}
.sucess
{
    font-size:3rem;
    color:#3c8a1e;
    position:relative;
    text-align:center;
}
.fail
{
      font-size:3rem;
    color:#8a1e1e;
    position:relative;
    text-align:center;
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

    cp = st.selectbox('CHEST PAIN TYPE',('TYPICAL ANGINA','ATYPICAL ANGINA','NON-ANGINAL PAIN','ASYMPTOMATIC'),  help="There are 4 types : typical angina, atypical angina , non-anginal pain and asymptomatic")
    if(cp=='TYPICAL ANGINA'):cp=0
    elif cp=='ATYPICAL ANGINA':cp=1
    elif cp=='NON-ANGINAL PAIN' :cp=2
    else : cp=3

    
    tres = st.number_input('RESTING BLOOD PREASSURE in mm Hg: ' ,min_value=120.00 , max_value=130.00 ,   help="Elevated blood pressure is when readings consistently range from 120-129 systolic and less than 80 mm Hg diastolic.")

    chol = st.number_input('SERUM CHOLESTORAL IN mg/dl: ' ,  min_value=120.00 ,max_value=201.00 ,    help="A person’s serum cholesterol level can indicate their risk of developing conditions such as heart disease. Range - 125 to 200mg/dL")

    fbs = st.selectbox('FASTING BLOOD SUGAR >120 mg/dl ',('TRUE' , 'FALSE') ,  help="This measures your blood sugar after an overnight fast (not eating).")
    if(fbs=='TRUE') : fbs=1
    else : fbs=0

    res = st.number_input('RESTING ELECTROCARDIOGRAPHIC RESULTS: ' ,  min_value=0 , help="An ECG can help detect: arrhythmias – where the heart beats too slowly, too quickly, or irregularly.")
    tha = st.number_input('MAXIMUM HEART RATE ACHIEVED: ' , help="It is the highest number of beats your heat can pump per minute when it's under high stress .")


    exa = st.selectbox('EXERCISE INDUCED ANGINA: ',('YES','NO') , help="Angina may feel like pressure in the chest, jaw or arm. It often occurs with exercise or stress.")
    if exa=='YES' : exa=1
    else : exa=0

    old = st.number_input('OLDPEAK ' ,  help=" ST depression induced by exercise relative to rest")
    slope = st.selectbox('SLOPE OF THE PEAK EXERCISE ST SEGMEN: ' , (0,1,2) ,  help="The slope of the peak exercise ST segment:1 = up sloping, 2 = flat, 3 = down sloping")
    
    ca = st.selectbox('NUMBER OF MAJOR VESSELS COLORED BY FLOUROSOPY',(0,1,2,3) ,  help="NUMBER OF MAJOR VESSELS COLORED BY FLUOROSCOPY THAT RANGED BETWEEN 0 AND 3")

    thal = st.selectbox('THAL',('NORMAL','FIXED DEFECT','REVERSABLE DEFECT') , help="  NORMAL BLOOD FLOW , FIXED DEFECT (NO BLOOD FLOW IN SOME PART OF THE HEART) , REVERSIBLE DEFECT (A BLOOD FLOW IS OBSERVED BUT IT IS NOT NORMAL)")
    if thal=='NORMAL': thal=1
    elif thal=="FIXED DEFECT":thal=2
    else :thal=3
    # st.write(thal)


    data = {'age': age,
            'sex': sex, 
            'cp': cp,
            'trestbps':tres,
            'chol': chol,
            'fbs': fbs,
            'restecg': res,
            'thalach':tha,
            'exang':exa ,
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
    if prediction==0 :
         st.write('<p class="sucess">EVERYTHING SEEMS HEALTHY! HAVE A GREAT DAY</p>', unsafe_allow_html=True )
         
         
    else  : 
         st.write('<p class="fail">VISIT A CARDIOLIGIST NOW </p>', unsafe_allow_html=True  )
         st.write("FIND [CARDIOLIGIST](https://www.google.com/search?q=cardiologist+near+me&rlz=1C1RXQR_enIN1028IN1028&oq=CARDIO&aqs=chrome.0.69i59j69i57j69i59j0i271l2j69i60j69i61.1218j0j1&sourceid=chrome&ie=UTF-8) NEAR ME")
        #  image = Image.open('download.png')
        #  st.image(image, caption='3 marla plot',use_column_width=True)


