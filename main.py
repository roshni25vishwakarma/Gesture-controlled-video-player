import streamlit as st


st.title("Gesture Controlled Video Player")
st.image('gc.jpeg', use_column_width=True)


sidebar = st.sidebar

sidebar.title('User Options')


def introduction():
    st.markdown("""
        ## Heading Level 2
        - Feature 1
        - Feature 2
        - Feature 3
    """)

    c1= st.columns(1)

    c1.header("Column 1 Content")



def execute():
    st.subheader('project working here')


options = ['Project Introduction', 'Execution']

selOption = sidebar.selectbox("Select an Option", options)

if selOption == options[0]:
    introduction()
elif selOption == options[1]:
    execute()
 
def setting():
    st.sidebar('hight')
    st.sidebar('width')
    st.sidebar('fps')
    selectbox = st.sidebar.selectbox("select hight ,width,fps"),["hight","width","fps"]
    st.write(f"You select{selectbox}")








options = ['Project Introduction','Execution','setting']
selOption = sidebar.selectbox("Select an Option", options)

if selOption == options[0]:
    introduction()
elif selOption == options[1]:
    execute()