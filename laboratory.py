import streamlit as st

menu =["Home Page","COVID-19 Test","Order Center"]
Choice = st.sidebar.selectbox("Menu",menu)
if Choice=="Home Page":
    st.title("Welcome to GeneLab")
    from PIL import Image
    img = Image.open("laboratory.png")
    st.image(img, width=900)
    st.subheader("Services")
    col3,col4=st.columns(2)
    with col3:
        st.markdown("#### ◼COVID-19 Test")
        from PIL import Image
        img = Image.open("covidimage.png")
        st.image(img, width=300)
    with col4: 
        st.markdown("#### ◼Products")
        from PIL import Image
        img = Image.open("products.png")
        st.image(img, width=300)
    st.markdown("##### Contact Us:")
    st.markdown("##### Phone Number:+23490911122234")
    st.markdown("##### Email Address:talkHealth@genelab.com")
    from PIL import Image
    img = Image.open("we care.png")
    st.image(img, width=250)
        
   
    
    
    
if Choice=="COVID-19 Test":
    from PIL import Image
    
    img = Image.open("COVIDLAB.png")
    
    st.image(img, width=800)
    
    st.title('Welcome to COVID-19 Test Booking')
    
    st.success("Application Form")
    
    Firstname=st.text_input("First Name")
    
    Surname=st.text_input("Surname")
    
    EmailAddress=st.text_input("Email address")
    
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
        st.success("Your COVID TEST BOOKING WAS SUCCESSFUL. Thank you for choosing GeneLab!!!🙂")
    from PIL import Image
    img = Image.open("covidrules2.png")
    st.image(img, width=700)
    

if Choice=="Order Center":
    Name=st.text_input("Name:")
    Email_address=st.text_input(" Email address:")
    st.subheader("Products Available:")
    col1,col2=st.columns(2)
    col1.write("#### Pippette")
    col2.write("#### 96 well plate")
    
    with col1:
        from PIL import Image
        img = Image.open("pippette.png")
        st.image(img, width=250)
        st.text("#20000 per item")
        cost2=20000
        quantity=st.number_input("Quantity of pippette")
        price1= quantity * cost2
#         if(st.button('Submit')):
#             st.success("Price is #{}".format(price1))     
              
        with col2:
            from PIL import Image
            img = Image.open("96wellplate.png")
            st.image(img, width=350)
            st.text("#5000 per item")
            cost3=5000
            quantity=st.number_input("Quantity of 96 well plate")
            price2= quantity * cost3
#             if(st.button('Submit.')):
#                 st.success("Price is #{}".format(price2)) 
                
        if col1 and col2:
            total_cost = price1 + price2
            st.success("Total price is #{}".format(total_cost))
            if(st.button('SUBMIT')):
                st.success("Your order has been processed")

    

