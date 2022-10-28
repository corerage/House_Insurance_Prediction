# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:22:51 2022

@author: Corerage
"""
#impoting the necessary dependecies
import streamlit as st
import pandas as pd 
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from plotly.offline import iplot, init_notebook_mode
from plotly.subplots import make_subplots
from plotly.offline import iplot
from plotly import tools
import plotly.express as px


#set page width to wide
st.set_page_config(layout='wide')

#Create sidebar
st.sidebar.markdown("<div><img src='https://o.remove.bg/downloads/53c9c412-09d5-48ee-a985-f884723167b3/kisspng-insurance-agent-vector-graphics-home-insurance-ins-pima-2-18-annual-meeting-5ce2246db91b44.2170783415583243337582-removebg-preview.png' width=100 /><h1 style='display:inline-block'>INSURANCE</h1></div>", unsafe_allow_html=True)
st.sidebar.markdown("This web app allows you to predict Insurance Prices using Python and Streamlit.")
st.sidebar.markdown("To get started <ol><li>Enter the <i>parameters</i> that best describe you</li> <li>Hit <i>the predict button</i>.</li> <li>Get your predictions</li></ol>",unsafe_allow_html=True)


#loading the dataset
df = pd.read_csv('https://raw.githubusercontent.com/stedy/Machine-Learning-with-R-datasets/master/insurance.csv')


#using a markdown to import a logo and a sunheader
st.markdown("<div><img src='https://o.remove.bg/downloads/53c9c412-09d5-48ee-a985-f884723167b3/kisspng-insurance-agent-vector-graphics-home-insurance-ins-pima-2-18-annual-meeting-5ce2246db91b44.2170783415583243337582-removebg-preview.png' width=200 /><h1 style='display:inline-block'>INSURANCE PREDICTION</h1></div>", unsafe_allow_html=True)
st.subheader("Welcome to my APP! Feel free to explore and be happy 😀")


#creating a columns
col1, col2=st.columns(2)


#load the dataframe
st.write(df)



#plotting a pie-chart with plotly
labels =['southwest', 'southeast', 'northwest', 'northeast']

col1=trace_pie = go.Pie(labels=labels,
                   values=df['region'].value_counts(),
                   textinfo='label+percent',hoverinfo='label+percent',
                   marker=dict(line=dict(width=1.5)),)

layout = go.Layout(titlefont=dict(size=30))

st.plotly_chart(dict(data=trace_pie, layout=layout))




#plotting histogram with plotly
col2=fig = px.histogram(df, x="children")
st.plotly_chart(fig, use_container_width=True)



#plotting scatterplot with plotly
fig = px.scatter(df, x="age", y="bmi")
st.plotly_chart(fig, use_container_width=True)



#importing the model
model = joblib.load('model_lin')



#creating a sidebar for input
st.sidebar.subheader("Insurance Params")
f1= st.sidebar.slider('Enter Your Age', 18,100)

s1= st.sidebar.selectbox('Sex',('Male', 'Female'))
if s1== 'Male':
    f2=1
else:
    f2=0
    
f3= st.sidebar.number_input('Enter Your BMI Number')
    
f4= st.sidebar.slider('Enter the Number of Children', 0,4)
    
s2= st.sidebar.selectbox("Are You a Smoker?",("Yes","No"))
    
if s2== 'Yes':
    f5=1
else:
    f5=0
    
    
s3= st.sidebar.selectbox("Enter Your Region",('southwest', 'southeast', 'northwest', 'northeast'))
    
if s3== 'southwest':
    f6=0
elif s3=='southeast':
    f6=1
elif s3=='northwest':
    f6=2
else:
    f6=3
    
#creating a button  
button= st.sidebar.button('Predict')
    
if button:
    pred= np.expm1(model.predict([[f1,f2,f3,f4,f5,f6]]))
#output from prediction                       
    text= st.success('Your Insurance Cost is **${:.2f}**'.format(pred[0]))
