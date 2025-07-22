
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Load Data
df = pd.read_csv("loan_test.csv")

# Data Cleaning
df['Applicant_Income'] = df['Applicant_Income'].fillna(df['Applicant_Income'].median())
df['Coapplicant_Income'] = df['Coapplicant_Income'].fillna(0)
df['Loan_Amount'] = df['Loan_Amount'].fillna(df['Loan_Amount'].median())
df['Credit_History'] = df['Credit_History'].fillna(1.0)
df['Dependents'] = df['Dependents'].replace('3+', 3).astype(float)

# Encoding
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})
df['Married'] = df['Married'].map({'Yes': 1, 'No': 0})
df['Self_Employed'] = df['Self_Employed'].map({'Yes': 1, 'No': 0})
df['Education'] = df['Education'].map({'Graduate': 1, 'Not Graduate': 0})
df['Area'] = df['Area'].map({'Urban': 2, 'Semiurban': 1, 'Rural': 0})
df['Total_Income'] = df['Applicant_Income'] + df['Coapplicant_Income']

# Streamlit Title
st.title("Loan Data Dashboard")

# Sidebar Filter
area_filter = st.sidebar.multiselect("Select Area(s):", options=df['Area'].unique(), default=df['Area'].unique())
df_filtered = df[df['Area'].isin(area_filter)]

# Metrics
st.subheader("Summary Statistics")
st.write(df_filtered.describe())

# Histogram
st.subheader("Loan Amount Distribution")
fig1, ax1 = plt.subplots()
sns.histplot(df_filtered['Loan_Amount'], kde=True, ax=ax1)
st.pyplot(fig1)

# Boxplot
st.subheader("Loan Amount by Education")
fig2, ax2 = plt.subplots()
sns.boxplot(x='Education', y='Loan_Amount', data=df_filtered, ax=ax2)
st.pyplot(fig2)

# Correlation
st.subheader("Correlation Heatmap")
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.heatmap(df_filtered.select_dtypes(include='number').corr(), annot=True, cmap='viridis', ax=ax3)
st.pyplot(fig3)

# Raw data
if st.checkbox("Show Raw Data"):
    st.write(df_filtered)
