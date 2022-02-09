import streamlit as st

from PIL import Image
img = Image.open("bmi.png")
st.image(img, width=700)

# give a title to our app
st.title('Welcome to Body Mass Index Calculator')

st.markdown('### Use this App to Calculate your BMI!')

# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kgs)")

# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Select your height format: ',('cms', 'meters', 'feet'))
if(status == 'cms'):
    # take height input in centimeters
    height = st.number_input('Centimeters')
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("You have not entered some value for your height")
        
elif(status == 'meters'):
    # take height input in meters
    height = st.number_input('Meters')

    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")

else:
    # take height input in feet
    height = st.number_input('Feet')

    # 1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")
        
        
if(st.button('Calculate BMI')):
    st.text("Your BMI Index is {}.".format(bmi))
    
    if(bmi < 16): #Interpret the Result
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overweight")


hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

        
        




    
