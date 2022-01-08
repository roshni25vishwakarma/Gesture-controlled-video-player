import streamlit as st


st.title("Gesture Controlled Video Player")
st.image('gc.jpeg', use_column_width=True)


sidebar = st.sidebar

sidebar.title('User Options')


def introduction():
    st.markdown("""
        ## Computer Vision
        -Computer vision is a field of artificial intelligence (AI) that enables computers and systems to derive meaningful information from digital images, videos and other visual inputs — and take actions or make recommendations based on that information.
    """)
def introduction():
    st.markdown("""
        ## Instructions
    
    Use One Finger for Volume Up.
    Use Two Fingers for Volume Down.
    Use Three Fingers for Volume Mute.
    Use Four Fingers for Play.
    Use Five Fingers for Pause.
    """)

    c1= st.columns(1)




def execute():
    st.subheader('project working here')


options = ['Project Introduction', 'Execution']

selOption = sidebar.selectbox("Select an Option", options)

if selOption == options[0]:
    introduction()
elif selOption == options[1]:
    execute()
 

