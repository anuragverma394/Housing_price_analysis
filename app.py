import time
import requests
import pandas as pd
import numpy as nprun 
import streamlit as st
import plotly.express as px
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner

#load requets
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://assets9.lottiefiles.com/packages/lf20_leneywe2.json"

lottie_hello = load_lottieurl(lottie_url_hello)

with st.container():
  right_column = st.container()
st_lottie(lottie_hello,height=300, key="Welcome")


 
 #with  right_column:
  #   st_lottie(lottie_url_hello,height=300,key="coding")


#loading data
@st.cache_data
def load_data():
    path ='data/kc_house_data.csv'
    df=pd.read_csv(path)
    return df

#call the load_data function
with st.spinner('Loading data...'):
     df=load_data()

#create a title for your app
st.title("House price data analysis     :dollar:")


#display the data
if st.checkbox('Show dataset',True):
     st.subheader('Dataset:moneybag:')
     st.dataframe(df)

#app

     