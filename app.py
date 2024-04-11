from streamlit_option_menu import option_menu
from pipelines import pipeline
import streamlit as st
nlp = pipeline("e2e-qg", model="valhalla/t5-base-e2e-qg")

st.title('Interview question generation Using NLP')
text=st.text_input('text')
  
if st.button('Generate Questions '):
    print(nlp(text))
st.success(text)
