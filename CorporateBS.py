# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 19:32:51 2022

@author: Miguelangel
"""
import streamlit as st
from PIL import Image
import pandas as pd
#import plotly.express as px
#import altair as alt

# Page Settings
st.set_page_config(layout="wide")
m = st.markdown("""
                <style>
                div.css-1r6slb0.e1tzin5v2{
                    background-color: #DCDCDC;
                    padding: 3% 3% 3% 3%;
                    border-radius: 5px;
                    }
                div.css-12w0qpk.e1tzin5v2{
                    background-color: #DCDCDC;
                    padding: 3% 3% 3% 3%;
                    border-radius: 5px;
                    }
                footer.css-qri22k.egzxvld0 {
                    visibility: hidden;
                    }
                div.css-79elbk.e1fqkh3o8 {
                    visibility: collapse;
                    }
                .css-k0sv6k.e8zbici2 {
                    background-color: #349D60;
                    color: white;
                    }
                .css-1siy2j7.e1fqkh3o3 {
                    background-color: rgba(52, 157, 96, 0.2);
                    }
                </style>
                """, unsafe_allow_html=True)

df = pd.read_csv("Karen_Lee_ManagerReport.csv")
df.drop(["Last Accessed", "Due Date", "Completed Date"], axis = 1, inplace = True)
dfcompleted = df[df["Completed"]=="yes"]

dfkaren = df[df["Manager"]=="Karen Lee"]
dfkarencomplete = dfkaren[dfkaren["Completed"]=="yes"]

dfruth = df[df["Manager"]=="Ruth Nolan"]
dfruthcomplete = dfruth[dfruth["Completed"]=="yes"]

dfblake = df[df["Manager"]=="Blake Rahman"]
dfblakecomplete = dfblake[dfblake["Completed"]=="yes"]

dfsarah = df[df["Manager"]=="Sarah Acres"]
dfsarahcomplete = dfsarah[dfsarah["Completed"]=="yes"]

def main_page():
    st.markdown("# Corporation :office:")
    st.sidebar.markdown("# Corporation :office:")
    
    # Row A
    a1, a2, a3, a4 = st.columns(4)
    a1.image(Image.open('D2L_Logo.png'))
    a2.metric("Employees", len(df["Username"].value_counts()), None)
    a3.metric("Teams", len(df["Team"].value_counts()), None)
    a4.metric("Managers", len(df["Manager"].value_counts()), None)
    
    # Row B
    b1, b2, b3, b4 = st.columns(4)
    b1.metric("Enrollments", len(df), None)
    b2.metric("Enrollments Finished", len(df[df["Completed"]=="yes"]), None)
    b3.metric("Percentaje %", len(df[df["Completed"]=="yes"])/len(df["Completed"])*100, None)
    b4.metric("Active Courses", len(df["Course Name"].value_counts()), None)
    
    
    #Row C
    graficas = st.container()
    with graficas:
        st.subheader('Top 6 Courses with Enrollments')
        chart1_data = df["Course Name"].value_counts().head(6)
        st.bar_chart(chart1_data)
        
        st.subheader('Top 6 Courses with Enrollment and Finished')
        chart2_data = dfcompleted["Course Name"].value_counts().head(6)
        st.bar_chart(chart2_data)


def manager():
    st.markdown("# Manager :ghost:")
    st.sidebar.markdown("# Manager :ghost:")
    
    #Row Karen
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("Manager", "Karen Lee", None)
    a2.metric("Employees", len(dfkaren["Username"].value_counts()), None)
    a3.metric("Enrollments", len(dfkaren), None)
    a4.metric("Finished", len(dfkarencomplete), "60.8%")
    #a5.metric("Percentaje", len(dfkarencomplete)/len(dfkaren)*100, None)
    
    #Row Ruth
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("Manager", "Ruth Nolan", None)
    a2.metric("Employees", len(dfruth["Username"].value_counts()), None)
    a3.metric("Enrollments", len(dfruth), None)
    a4.metric("Finished", len(dfruthcomplete), "63.1%")
    #a5.metric("Percentaje", len(dfkarencomplete)/len(dfkaren)*100, None)
    
    #Row Blake
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("Manager", "Blake Rahman", None)
    a2.metric("Employees", len(dfblake["Username"].value_counts()), None)
    a3.metric("Enrollments", len(dfblake), None)
    a4.metric("Finished", len(dfblakecomplete), "61.1%")
    #a5.metric("Percentaje", len(dfkarencomplete)/len(dfkaren)*100, None)
    
    #Row Sarah
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("Manager", "Sarah Acres", None)
    a2.metric("Employees", len(dfsarah["Username"].value_counts()), None)
    a3.metric("Enrollments", len(dfsarah), None)
    a4.metric("Finished", len(dfsarahcomplete), "73.3%")
    #a5.metric("Percentaje", len(dfkarencomplete)/len(dfkaren)*100, None)
    

def courses():
    st.markdown("# Courses :school:")
    st.sidebar.markdown("# Courses :school:")
    
def employees():
    st.markdown("# Employees :rocket:")
    st.sidebar.markdown("# Employees :rocket:")

page_names_to_funcs = {
    "Corporation": main_page,
    "Manager Stats": manager,
    "Course Stats": courses,
    "Employee Stats": employees,
}

selected_page = st.sidebar.selectbox("Select a dashboard", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
