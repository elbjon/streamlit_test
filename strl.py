import streamlit as st



user_movies_matrix = pd.read_csv('umm.csv')


df = pd.read_csv('ratings.csv')

df_movies = pd.read_csv('movies.csv')