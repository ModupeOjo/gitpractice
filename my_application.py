import streamlit as st

# Add Title
st.title("Welcome to Preston Hotel Lagos")

from PIL import Image
img = Image.open("hotel.png")
st.image(img, width=800)

if st.checkbox("Select/Unselect"):
    st.text("Selection Ready")
# Dictionary
status = st.radio("Select Dish: ", ('Africana', 'Asia'))

if (status == 'Africana'):
    st.success("Africana")
else:
    st.success("Asia")
dish = st.selectbox("Select Dish: ",
                     ['Jollof Rice', 'Bunny chow', 'Afang Soup'])
name = st.text_input("Enter Your name", "Type Here ...")
if(st.button('Submit')):
    result = name.title()
    st.success(result)

# st.header("Thank you for choosing Preston Hotel Lagos")
st.markdown('### Thank you for choosing Preston Hotel Lagos!')

level = st.slider("How Satisfied are you on a Scale of 5?", 1, 5)
 
st.text('Selected: {}'.format(level)) 


