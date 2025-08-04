import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit import title

data=pd.read_csv("../diabetes.csv")
#print (data)

st.set_page_config(page_title="diabetes dashboard",layout="wide")
st.title("Diabetes Dashboard")

st.subheader("Statistics of the number of people with Diabetes")

tab1,tab2,tab3=st.tabs(['Glucose','BMI','Age'])

with tab1:
    st.subheader("Glucose Analysis")
    c1,c2=st.columns(2)
    with c1:
        glucose=data['Glucose']
        glucose=glucose.mean()
        glucose=round(glucose,2)
        c1.metric('Average Glucose',glucose)
    with c2:
        glucose_fig=px.histogram(data,x='Glucose',nbins=40,color_discrete_sequence=["#f5e680"])
        glucose_fig.update_layout(title="Glucose level distribution",xaxis_title='Glucose',yaxis_title="Number")
        st.plotly_chart(glucose_fig)

with tab2:
    st.subheader("BMI Analysis")
    c1,c2 = st.columns(2)
    with c1:
        BMI = data['BMI']
        BMI = BMI.mean()
        BMI = round(BMI, 2)
        c1.metric('Average BMI', BMI)
    with c2:
        BMI_fig=px.histogram(data,x='BMI',nbins=40,color_discrete_sequence=["#7beef5"])
        glucose_fig.update_layout(title="BMI level distribution",xaxis_title='BMI',yaxis_title="Number")
        st.plotly_chart(BMI_fig)

with tab3:
    st.subheader("Age Analysis")
    c1,c2 = st.columns(2)
    with c1:
        age = data['Age']
        age = age.mean()
        age = int(age)
        c1.metric('Average Age', age)
    with c2:
        age_fig=px.histogram(data,x='Age',nbins=40,color_discrete_sequence=["skyblue"])
        glucose_fig.update_layout(title="Age level distribution",xaxis_title='Age',yaxis_title="Number")
        st.plotly_chart(age_fig)