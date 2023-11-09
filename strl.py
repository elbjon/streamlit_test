import streamlit as st
import pandas as pd

test = pd.read_csv('umm.csv')
st.write(test.head(3))

st.title('My Work')

st.write('hello streamlit')

color=st.text_input('whats you fav col?')

st.write(color, 'you like')
