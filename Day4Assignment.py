#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import seaborn as sns 
#Remove Warnings
st.balloons()#will throw ballons on the restart
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Years of expreience vs Salary")

#import dataset
df = pd.read_csv('Salary_Data.csv')
#First thirty rows
tips = df.head(31)
#Display the table
st.table(tips)
st.header("Visualisation Using Seaborn")
#bar plot
st.subheader("Bar Plot")
tips.plot(kind='bar')
st.pyplot()
#Displot
st.subheader("Displot")
sns.displot(tips["YearsExperience"])
st.pyplot()
#joinplot
st.subheader("JointPlot")
sns.jointplot(x='YearsExperience',y='Salary',data=tips,kind='scatter')
st.pyplot()#it is to plot the graph
#pairplot
st.subheader("Pairplot")
sns.pairplot(tips,hue='Salary')
st.pyplot()
#Rugplot
st.subheader("Rugplot")
sns.rugplot(tips['Salary'])#distribution of a single data
st.pyplot()
#Correation
st.subheader("Heatmap")
sns.heatmap(tips.corr(),cmap='coolwarm',annot=True)
st.pyplot()
