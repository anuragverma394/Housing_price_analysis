import time
import requests
import pandas as pd
import numpy as nprun 
import streamlit as st
import plotly.express as px
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://assets9.lottiefiles.com/packages/lf20_leneywe2.json"

lottie_hello = load_lottieurl(lottie_url_hello)

st_lottie(lottie_hello, key="Welcome")

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
st.title('House price data analysis')


#display the data
if st.checkbox('Show dataset',True):
     st.subheader('Dataset')
     st.dataframe(df)

#app

     