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

dfsandbox = pd.read_csv("compare_dataset.csv", index_col= "Category")

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
    

def overview():
    a1, a2, a3, a4 = st.columns(4)
    a1.image(Image.open('D2L_Logo.png'))
    a2.metric("Region", "LATAM", None)
    a3.metric("Prospect", "MMM", None)
    a4.metric("Status", "Active", None)
    
    st.markdown("# General Overview :school:")
    #General Overview
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("Users OOTB", dfsandbox.loc["Users"]["OOTB"], None)
    a2.metric("Users Sandbox", dfsandbox.loc["Users"]["Sandbox"], None)
    a3.metric("Delta", dfsandbox.loc["Users"]["Diff"], None)
    a4.metric("Percentage", dfsandbox.loc["Users"]["Percentage"], None)
    
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("Students OOTB", dfsandbox.loc["Students"]["OOTB"], None)
    a2.metric("Students Sandbox", dfsandbox.loc["Students"]["Sandbox"], None)
    a3.metric("Delta", dfsandbox.loc["Students"]["Diff"], None)
    a4.metric("Percentage", dfsandbox.loc["Students"]["Percentage"], None)
    
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("StudentsLogins OOTB", dfsandbox.loc["StudentsLogins"]["OOTB"], None)
    a2.metric("StudentsLogins Sandbox", dfsandbox.loc["StudentsLogins"]["Sandbox"], None)
    a3.metric("Delta", dfsandbox.loc["StudentsLogins"]["Diff"], None)
    a4.metric("Percentage", dfsandbox.loc["StudentsLogins"]["Percentage"], None)
    
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("Instructors OOTB", dfsandbox.loc["Instructors"]["OOTB"], None)
    a2.metric("Instructors Sandbox", dfsandbox.loc["Instructors"]["Sandbox"], None)
    a3.metric("Delta", dfsandbox.loc["Instructors"]["Diff"], None)
    a4.metric("Percentage", dfsandbox.loc["Instructors"]["Percentage"], None)
    
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("InstructorsLogins OOTB", dfsandbox.loc["InstructorsLogins"]["OOTB"], None)
    a2.metric("InstructorsLogins Sandbox", dfsandbox.loc["InstructorsLogins"]["Sandbox"], None)
    a3.metric("Delta", dfsandbox.loc["InstructorsLogins"]["Diff"], None)
    a4.metric("Percentage", dfsandbox.loc["InstructorsLogins"]["Percentage"], None)
    
    st.markdown("# Chart Users :school:")
    chart3_data = dfsandbox.loc[["Users", "Students", "Instructors"]][["OOTB", "Sandbox"]]
    st.bar_chart(chart3_data)
    
    st.markdown("# Chart Logins :school:")
    chart4_data = dfsandbox.loc[["StudentsLogins", "InstructorsLogins"]][["OOTB", "Sandbox"]]
    st.bar_chart(chart4_data)
    
    st.sidebar.markdown("# Sandbox Overview :school:")
    
def students():
    a1, a2, a3, a4 = st.columns(4)
    a1.image(Image.open('D2L_Logo.png'))
    a2.metric("Region", "LATAM", None)
    a3.metric("Prospect", "MMM", None)
    a4.metric("Status", "Active", None)
    
    st.markdown("# Students :rocket:")
    
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("Students OOTB", dfsandbox.loc["Students"]["OOTB"], None)
    a2.metric("Students Sandbox", dfsandbox.loc["Students"]["Sandbox"], None)
    a3.metric("Delta", dfsandbox.loc["Students"]["Diff"], None)
    a4.metric("Percentage", dfsandbox.loc["Students"]["Percentage"], None)
    
    st.markdown("# Content Stats :rocket:")
    
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("ContentCompleted OOTB", dfsandbox.loc["StudentsContentCompleted"]["OOTB"], None)
    a2.metric("ContentCompleted Sandbox", dfsandbox.loc["StudentsContentCompleted"]["Sandbox"], None)
    a3.metric("Delta", dfsandbox.loc["StudentsContentCompleted"]["Diff"], None)
    a4.metric("Percentage", dfsandbox.loc["StudentsContentCompleted"]["Percentage"], None)
    
    chart5_data = dfsandbox.loc["StudentsContentCompleted"][["OOTB", "Sandbox"]]
    st.area_chart(chart5_data)

    a1, a2, a3, a4 = st.columns(4)
    a1.metric("TimeInContent OOTB", dfsandbox.loc["StudentsTimeInContent"]["OOTB"], None)
    a2.metric("TimeInContent Sandbox", dfsandbox.loc["StudentsTimeInContent"]["Sandbox"], None)
    a3.metric("Delta", dfsandbox.loc["StudentsTimeInContent"]["Diff"], None)
    a4.metric("Percentage", dfsandbox.loc["StudentsTimeInContent"]["Percentage"], None)
    
    
    st.markdown("# Quizzes Stats :rocket:")
    
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("QuizCompleted OOTB", dfsandbox.loc["StudentsQuizCompleted"]["OOTB"], None)
    a2.metric("QuizCompleted Sandbox", dfsandbox.loc["StudentsQuizCompleted"]["Sandbox"], None)
    a3.metric("Delta", dfsandbox.loc["StudentsQuizCompleted"]["Diff"], None)
    a4.metric("Percentage", dfsandbox.loc["StudentsQuizCompleted"]["Percentage"], None)
    
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("QuizAttempt OOTB", dfsandbox.loc["StudentsQuizAttempt"]["OOTB"], None)
    a2.metric("QuizAttempt Sandbox", dfsandbox.loc["StudentsQuizAttempt"]["Sandbox"], None)
    a3.metric("Delta", dfsandbox.loc["StudentsQuizAttempt"]["Diff"], None)
    a4.metric("Percentage", dfsandbox.loc["StudentsQuizAttempt"]["Percentage"], None)
    
    chart6_data = dfsandbox.loc[["StudentsQuizCompleted", "StudentsQuizAttempt"]][["OOTB", "Sandbox"]]
    st.bar_chart(chart6_data)
    
    st.area_chart(chart6_data)
    
    st.markdown("# Forums Stats :rocket:")
    
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("PostCreated OOTB", dfsandbox.loc["StudentsDiscussionPostCreated"]["OOTB"], None)
    a2.metric("PostCreated Sandbox", dfsandbox.loc["StudentsDiscussionPostCreated"]["Sandbox"], None)
    a3.metric("Delta", dfsandbox.loc["StudentsDiscussionPostCreated"]["Diff"], None)
    a4.metric("Percentage", dfsandbox.loc["StudentsDiscussionPostCreated"]["Percentage"], None)
    
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("PostRead OOTB", dfsandbox.loc["StudentsPostRead"]["OOTB"], None)
    a2.metric("PostRead Sandbox", dfsandbox.loc["StudentsPostRead"]["Sandbox"], None)
    a3.metric("Delta", dfsandbox.loc["StudentsPostRead"]["Diff"], None)
    a4.metric("Percentage", dfsandbox.loc["StudentsPostRead"]["Percentage"], None)  
    
    st.markdown("# Assignment Stats :rocket:")
    
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("AssignmentSubmission OOTB", dfsandbox.loc["StudentsAssignmentSubmission"]["OOTB"], None)
    a2.metric("AssignmentSubmission Sandbox", dfsandbox.loc["StudentsAssignmentSubmission"]["Sandbox"], None)
    a3.metric("Delta", dfsandbox.loc["StudentsAssignmentSubmission"]["Diff"], None)
    a4.metric("Percentage", dfsandbox.loc["StudentsAssignmentSubmission"]["Percentage"], None)
    
    st.sidebar.markdown("# Students :rocket:")

def instructors():
    a1, a2, a3, a4 = st.columns(4)
    a1.image(Image.open('D2L_Logo.png'))
    a2.metric("Region", "LATAM", None)
    a3.metric("Prospect", "MMM", None)
    a4.metric("Status", "Active", None)
    
    st.markdown("# Instructors :rocket:")

    a1, a2, a3, a4 = st.columns(4)
    a1.metric("Instructors OOTB", dfsandbox.loc["Instructors"]["OOTB"], None)
    a2.metric("Instructors Sandbox", dfsandbox.loc["Instructors"]["Sandbox"], None)
    a3.metric("Delta", dfsandbox.loc["Instructors"]["Diff"], None)
    a4.metric("Percentage", dfsandbox.loc["Instructors"]["Percentage"], None)
    
    st.markdown("# Grading Status :rocket:")   
    
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("GradeItems OOTB", dfsandbox.loc["InstructorsGradeItems"]["OOTB"], None)
    a2.metric("GradeItems Sandbox", dfsandbox.loc["InstructorsGradeItems"]["Sandbox"], None)
    a3.metric("Delta", dfsandbox.loc["InstructorsGradeItems"]["Diff"], None)
    a4.metric("Percentage", dfsandbox.loc["InstructorsGradeItems"]["Percentage"], None)

    a1, a2, a3, a4 = st.columns(4)
    a1.metric("GradedItems OOTB", dfsandbox.loc["InstructorsGradedItems"]["OOTB"], None)
    a2.metric("GradedItems Sandbox", dfsandbox.loc["InstructorsGradedItems"]["Sandbox"], None)
    a3.metric("Delta", dfsandbox.loc["InstructorsGradedItems"]["Diff"], None)
    a4.metric("Percentage", dfsandbox.loc["InstructorsGradedItems"]["Percentage"], None)    
    
    st.markdown("# Forums Status :rocket:")  
    
    a1, a2, a3, a4 = st.columns(4)
    a1.metric("Posts OOTB", dfsandbox.loc["InstructorsDiscussionPost"]["OOTB"], None)
    a2.metric("Posts Sandbox", dfsandbox.loc["InstructorsDiscussionPost"]["Sandbox"], None)
    a3.metric("Delta", dfsandbox.loc["InstructorsDiscussionPost"]["Diff"], None)
    a4.metric("Percentage", dfsandbox.loc["InstructorsDiscussionPost"]["Percentage"], None) 
    
    st.sidebar.markdown("# Instructors :rocket:")
    
page_names_to_funcs = {
    "Corporation": main_page,
    "Manager Stats": manager,
    "Sandbox Overview": overview,
    "Sandbox Students": students,
    "Sandbox Instructors": instructors,
}

selected_page = st.sidebar.selectbox("Select a dashboard", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
