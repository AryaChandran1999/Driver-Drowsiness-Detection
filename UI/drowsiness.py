from tkinter import Menu
import requests
from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Driver Drowsiness Detection',page_icon=':oncoming_taxi:',layout='wide')

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("Styles/styles.css")

selected = option_menu(
        menu_title=None,  
        options=["Home", "Methodology", "Trial","Contact"],  
        icons=["house", "book","webcam", "envelope"],  
        menu_icon="cast",  
        default_index=0,  
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color":"#483d8b	"},
            "icon": {"color": "black", "font-size": "15px"},
            "nav-link": {
                "font-size": "15px",
                "text-align": "center",
                "margin": "0px",
                "--hover-color": "#a9a9a9",
            },
            "nav-link-selected": {"background-color": "	#6a5acd"},
        },
    )
#return selected

st.markdown(""" <style> .font {
font-size:17px ; font-family: 'Arial'; color: #FFFFFF;} 
</style> """, unsafe_allow_html=True)

home_img = Image.open("Images/img4.jpg")

if selected == "Home":
    st.write('##')
    st.markdown("<h1 style='text-align: center; color: #dda0dd;'>DRIVER DROWSINESS DETECTION</h1>", unsafe_allow_html=True)
    st.image(home_img)
    st.write("##")
    st.write("##")
    st.write("##")

    st.markdown('<p class="font">These days, we see people from various professions facing long nights at work, jobs that are fundamental to the well-being and comfort of the society. As a result, they are left with only one option, to get behind the wheel while feeling tired and sleepy. This is something most drivers would have gone through atleast once in their lives. However, this is incredibly dangerous.</p>', unsafe_allow_html=True)
    st.markdown("<p class ='font'>For some who find themselves getting drowsy, a brief state of unconsciousness, called a microsleep, may occur. In these instances, the driver might still even have their eyes open, but they are not in proper control of their vehicle. Exhaustion can be as bad as driving under the influence of alcohol. Research has shown that 24 hours of sleep deprivation causes the same level of impairment as someone whose blood alcohol (BAC) level is at 0.10 percent a number that’s over the legal limit.</p>", unsafe_allow_html=True)

    st.markdown("<p class ='font'>There are safeguards in place for those whose jobs rely on long periods of driving. For example, truck drivers are forbidden from driving past 14 hours after their shift starts. But for the average driver, there are no such safeguards. Drowsiness is a significant cause of accidents, with studies finding that loss of concentration is responsible for 25% of road accidents. Preventing drowsy drivers from getting behind the wheel is important. Being able to detect drowsy drivers and remind them to be safe and take a break if they’re feeling sleepy is one way to address this issue.</p>", unsafe_allow_html=True)
if selected == "Projects":
    st.title(f"You have selected {selected}")

if selected == "Contact":
    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")
        contact_form = """
        <form action="https://formsubmit.co/aryachandran1999@gmail.com" method="POST">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your e-mail ID" required>
            <textarea name="message" placeholder="Your message" required></textarea>
            <button type="submit">Send</button>
        </form>
        """

        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
