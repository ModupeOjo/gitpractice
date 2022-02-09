import streamlit as st
import pandas as pd




menu =["Home Page","Covid Test","Order Center"]
Choice = st.sidebar.selectbox("Menu",menu)
if Choice=="Home Page":
    st.title("Welcome to GeneLab")
#     st.subheader("Your Health is Wealth")
    st.markdown(f'<h1 style="color:Red;font-size:30px;">{"Your Health is Wealth"}</h1>', unsafe_allow_html=True)
    from PIL import Image
    img = Image.open("laboratory.png")
    st.image(img, width=800)
    st.subheader("Services")
    col3,col4=st.columns(2)
    with col3:
        st.markdown("##### Covid-19 Test")
    with col4: 
        st.markdown("##### Products")   
    from PIL import Image
    img = Image.open("contact.png")
    st.image(img, width=300)
        
    
#     st.markdown('<a href="mailto:talkhealth@genelab.com">Contact us !</a>', unsafe_allow_html=True)
   
#     st.image([covidrules.png],[covidrules2])
    
    
if Choice=="Covid-19 Test":
    from PIL import Image
    img = Image.open("COVIDLAB.png")
    st.image(img, width=800)
    st.title('Welcome to COVID-19 Test Booking')
    st.success("Application Form")
    Firstname=st.text_input("First Name")
    Surname=st.text_input("Surname")
    Age =st.selectbox("Choose your age: ", range(1, 100, 1))
    DOB = st.date_input('Date of birth')
    Phone = st.text_input("Enter your phone number","Type Here")
    TestTime = st.time_input('Time scheduled for test') 
    cost=45000
    status = st.selectbox("SELECT TEST TYPE: ", ('Rapid Test', 'PCR Test'))
    if status== "Rapid Test":
        st.success("Rapid Test")
        st.success("Your test costs #20,000 only")
    if status=="PCR Test":
        Test_type= st.selectbox("SELECT: ", ('Standard', 'Priority'))
        if (Test_type=='Standard'):
                st.success("Your PCR test cost is #{}.".format(cost))
        else:
                priority=cost+5000
                st.success("Your PCR test cost is #{}.".format(priority))
    if(st.button('Submit')):
        st.success("Your COVID TEST BOOKING WAS SUCCESSFUL")
    from PIL import Image
    img = Image.open("covidrules2.png")
    st.image(img, width=700)
    
    
if Choice=="Order Center":
    st.title("ORDER FOR REAGENTS OR EQUIPMENTS")
    st.subheader("EQUIPMENT AVAILABLE")
    col1,col2=st.columns(2)
    col1.write("Pippette")
    col2.write("96 well plate")
    with col1:
        from PIL import Image
        img = Image.open("pippette.png")
        st.image(img, width=250)
        cost2=20000
        quantity=st.number_input("Quantity of pippette")
        price1= quantity * cost2
        if(st.button('Submit')):
            st.success("Total price is #{}".format(price1))     
              
        with col2:
            from PIL import Image
            img = Image.open("96wellplate.png")
            st.image(img, width=350)
            cost3=10000
            quantity=st.number_input("Quantity of 96 well plate")
            price2= quantity * cost3
            if(st.button('Submit.')):
                st.success("Total price is #{}".format(price2)) 
        if col1 and col2:
            total_cost = price1 + price2
            st.success("Total price is #{}".format(total_cost))
    st.success("Your order has been processed")

     

    
            
    
#     if (status=='Rapid Test'):
#         st.success("Rapid Test")
#         st.success("Your test costs #45,000 only")
#     if (status=='PCR Test'):
#         Test_type= st.selectbox("SELECT: ", ('Standard', 'Priority')
        
#         if (status=='Rapid Test'):
#             st.success("Rapid Test")
#             st.success("Your test costs #45,000 only")
#         if (status=='PCR Test'):
#             Test_type= st.selectbox("SELECT: ", ('Standard', 'Priority'))
            
#     First_name = st.text_input("First Name:\n")
   
#     with st.form(key='form1'):
#         Firstname=st.text_input("First Name")
#         Surname=st.text_input("Surname")
#         Age =st.selectbox("Choose your age: ", range(1, 100, 1))
#         DOB = st.date_input('Date of birth')
#         Phone = st.text_input("Enter your phone number","Type Here")
#         TestTime = st.time_input('Time scheduled for test') 
                          
#         cost=45000
                          
#         status = st.selectbox("SELECT TEST TYPE: ", ('Rapid Test', 'PCR Test'))
#         if (status=='Rapid Test'):
#             st.success("Rapid Test")
#             st.success("Your test costs #45,000 only")
#         if (status=='PCR Test'):
#             Test_type= st.selectbox("SELECT: ", ('Standard', 'Priority'))
            
#             Test_type= st.selectbox("SELECT: ", ('Standard', 'Priority'))
#             if (Test_type=='Standard'):
#                 st.success("Your PCR test cost is #{}.".format(cost))
#             else:
#                 priority=cost+5000
#                 st.success("Your PCR test cost is #{}.".format(priority))
# #                 form = st.form(key='form1')
#         submit_button = st.form_submit_button()
#     if(st.button('Submit')):
#         result = "Your COVID TEST BOOKING WAS SUCCESSFUL"
#         st.success(result) 
# from PIL import Image
# img = Image.open("covidrules2.png")
# st.image(img, width=700)
# # else:
#     st.title("About")
    
        
        
        
        
        
# form = st.form(key='Home')
# form.text_input(label='Home')
# submit_button = form.form_submit_button(label='Submit')
        
            
           
#             st.text("Your PCR test cost is #{}.".format(cost))

# if(st.button('Submit')):
#     result = Home
#     st.success(result)       

           
     
        
#     st.date_input('Date of birth')
       
        
        
#         st.number_input("")
# age = st.selectbox("Choose your age: ", range(18, 66,1))
    
    
# import streamlit as st
# import os
# import time
# import glob
# import os


# from gtts import gTTS
# from googletrans import Translator

# try:
#     os.mkdir("temp")
# except:
#     pass
# st.title("Text to speech")
# translator = Translator()

# text = st.text_input("Enter text")
# in_lang = st.selectbox(
#     "Select your input language",
#     ("English", "Hindi", "Bengali", "korean", "Chinese", "Japanese"),
# )
# if in_lang == "English":
#     input_language = "en"

# import streamlit as st  

# # import time

# list_a=[]
# list_b=[]

# st.title("WELCOME TO MODEE'S HAIR SALOON")
# client=st.number_input('Number of clients?')

# if number==1:
#     print("black")
#     list_a.append("black")
#     print(list_a)
# #         total=total+total[list_a]
# #         count_b=list_a.count("black")
# #         print(count_b)
# if number==2:
#     print("brown")
#     list_b.append("brown")
#     print(list_b)
# print("Total number of black hair:",len(list_a))
# print("Total number of brown hair:",len(list_b))

# st.title("WELCOME TO RAMAT SUPERMARKET")
# grocery_item = {}
# grocery_history = [] 

# stop = False 

# while not stop:
#     item_name = st.text_input("Item name:\n")
#     quantity = st.number_input("Quantity purchased:\n")   
#     cost = st.number_input("Price per item:\n")
#     grocery_item ={'name':item_name, 'number': int(quantity), 
#                     'price': float(cost)}
#     grocery_history.append(grocery_item)
#     st.text("Would you like to enter another item?\n 'Yes' for continue or 'No' to quit:\n")
#     status=st.radio('Selection:', ('Yes','No'))
#     if (status == 'No'):
#         st.success("No")
#         stop = True
       
# grand_total = 0  
 
# for index, item in enumerate(grocery_history):
#         item_total = item['number'] * item['price']
#         grand_total = grand_total + item_total
        
# if (st.button('calculate grant_total')):
#     st.text("Total price is {}.".format(grand_total))
#     st.write('Grand Total: #%.2f' % grand_total)
    
# #     if (st.button('calculate grant_total')):
# #         st.text("Total price is {}.".format(grand_total))

        