import streamlit as st
import pandas as pd








usermoviesmatrix = pd.read_csv('umm.csv')

df = pd.read_csv('ratings.csv')

dfmovies = pd.read_csv('movies.csv')

url = 'https://drive.google.com/file/d/1hgz5gpLuuZTxSEx9jixkWaTIfjAhkYV8/view?usp=sharing'
path = 'https://drive.google.com/uc?id='+url.split('/')[-2]
moviescorrelationsmatrix = pd.read_csv(path)
