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
st.subheader('Key performance indicators')

#get the list of all columns
cols = df.columns.tolist()
selected_cols = st.multiselect('Select Columns',cols)

#st.write(f'You selected: {len(selected_cols)} colums')

#st.metric(label='Average Price',value=round(df['price'].mean()),
    #      delta=round(df['price'].std()))

for col in selected_cols:
    try:
          
     st.subheader(f'Column: {col}')
     st.metric(label = f'Mean {col}',
                  value= round(df[col].mean()),
                  delta= round(df[col].std()))
     st.area_chart(df[col],use_container_width=True)
    except:
        st.error(f'Cannot display {col} numeric data')
          
