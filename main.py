import  streamlit as st

st.title("Welcome to my app")

st.header("Building is in progress......")

st.subheader('App is on the way...')

st.text("This is text")

st.markdown("this is markdown")

st.markdown("# this is markdown")

st.success('Successfull')

st.info('Information')

st.warning('warning')

st.error('dis is error')

if st.checkbox('show/hide'):
    st.text('Showing/hiding widget')
status= st.radio('Display your status',('Yes','No'))

if status == 'Yes':
    st.success('Proceed')
else:
    st.warning('Dont proceed further')

occupation = st.selectbox('your role',['DE','SDE','DS','DA'])

st.write('you are working as',occupation)

cities = st.multiselect('your city',['delhi','hyd','chennai','maripivalasa','vizag','panaji','cochin'])
st.write(cities,'is your working city')
st.write('working in ',len(cities),'cities')
st.slider('range',1,5)

about = st.button('Make dive into it')
if about == 'About':
    st.text('Hello how are you')
else:
    st.text('Please review mine')

if st.button('Submit'):
    st.text('submitted the application')

first = st.text_input('Enter the name','You can enter your name')
if st.button('submit',key= '1'):
    result = first.title()
    st.success(result)

# msg = st.text_area('Enter the decription','You can enter your name')
# if st.button('submit',Key="2"):
#     result = msg.title()
#     st.success(result)
import datetime
today = st.date_input('Today is',datetime.datetime.now())

time = st.time_input('Time is',datetime.time())

st.text('Display json date')
st.json({'name':'Manohar',
         'gender':'male'})

with st.echo():
    import pandas as pd
    df = pd.DataFrame()

st.button('Predict')