import streamlit as st
import pandas as pd


url = 'https://drive.google.com/file/d/1hgz5gpLuuZTxSEx9jixkWaTIfjAhkYV8/view?usp=sharing'
path = 'https://drive.google.com/uc?id='+url.split('/')[-2]
movies_cosines_matrix = pd.read_csv(path)


st.write(user_movies_matrix.shape)
st.write(user_movies_matrix.info())
st.write(user_movies_matrix.describe())
st.write(user_movies_matrix.head(2))

user_movies_matrix = pd.read_csv('umm.csv')

df = pd.read_csv('ratings.csv')

df_movies = pd.read_csv('movies.csv')

st.write('end of program')
