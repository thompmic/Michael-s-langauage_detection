import pickle
import string
import streamlit as st
import webbrowser

global Lrdetect_Model

LrdetectFile = open('model.pck2','rb')
Lrdetect_Model = pickle.load(LrdetectFile)
LrdetectFile.close()
st.title(" Michael Language Detection Tool")
input_test = st.text_input("Provide your text input here", 'Hello my name is Mike ')

button_clicked = st.button("Get Language Name")
if button_clicked:
    st.text(Lrdetect_Model.predict([input_test]))
