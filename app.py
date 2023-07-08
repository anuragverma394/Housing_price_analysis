import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

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
     