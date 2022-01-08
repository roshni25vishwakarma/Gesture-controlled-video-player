import streamlit as st
from vlc2 import GestureRecognition

st.title("Gesture Controlled Video Player")
st.image('gc.jpeg', use_column_width=True)


sidebar = st.sidebar

sidebar.title('User Options')


def Introduction():
    st.title("computer vision")
    st.image('sv.jpg', use_column_width=True)
    st.markdown("""
    
        -Computer vision is a field of artificial intelligence (AI) that enables computers and systems to derive meaningful information from digital images, videos and other visual inputs — and take actions or make recommendations based on that information.
    """)

    c1= st.columns(1)

def execute():
    st.subheader('project working here')
    st.title("USAGE")
    st.markdown("""
    """)
    st.markdown("""
      video controll by gesture steps.
    """)
    st.markdown("""1-Detection  of  hand  from  streaming  video  by  using Lucas  Kanade  Pyramidical  Optical  Flow.
     2-algorithm it detects moving points (hand) in image.   
     3-It passes the above moving points to K-MEAN  .
     4-algorithm to find center of motion which is equivalent to the center of moving hand.   Generate  a  rectangle  around this  motion  center and crop the region within this rectangle.  
     5-After cropping  save image to a specific location for learning or directly use for recognition.  
    6-Learning  Phase:  After  getting  efficient  images  from  above operations  these  are  used  for  training.
    """)


    run = st.checkbox('Run Gesture Recognitiom')
    if run:
        GestureRecognition()

options = ['Project Introduction', 'Execution']

selOption = sidebar.selectbox("Select an Option", options)

if selOption == options[0]:
    Introduction()
elif selOption == options[1]:
    execute()
    
    


    