# ==================================================
#  Streamlit for Dashboard with Python | Codanics
# ==================================================
#https://youtu.be/9tF1CtthAMw?list=PL9XvIvvVL50FG8TUsLScsLMmJDacK36x2
# ==================================================
#           Importing Required Libraries
# ==================================================
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
# ==================================================
#           Read The Data | CSV File
# ==================================================
df = pd.read_csv("diabetes.csv")
st.title("PIMA INDIAN DIABETES DATA SET")
st.subheader("Diabetes Prediction APP . . .")
st.write(df.head())
st.header("Exploring Diabetes DataSet . . .")
st.sidebar.header("Patient Data")
st.subheader("Description Stats of Data . . .")
st.write(df.describe())

X = df.drop(['Outcome'], axis = 1)
y = df.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=.2, random_state=0)


def user_report():
    pregnancies = st.sidebar.slider("Pregnancies", 0, 17, 2)
    glucose = st.sidebar.slider("Glucose", 0, 199,110)
    bp = st.sidebar.slider("BloodPressure", 0, 122, 80)
    skinthinkness = st.sidebar.slider("SkinThickness", 0, 99, 12)
    insulin = st.sidebar.slider("Insulin", 0, 846, 80)
    bmi = st.sidebar.slider("BMI", 0, 67, 5)
    dpf = st.sidebar.slider("DiabetesPedigreeFunction", 0.07, 2.42,0.37)
    age = st.sidebar.slider("Age", 21, 81, 33)

    user_report_data = {
        "pregnancies" : pregnancies,
        "glucose" : glucose,
        "bp" : bp,
        "skinthinkness" : skinthinkness,
        "insulin" : insulin,
        "bmi" : bmi,
        "dpf" : dpf,
        "age" : age
    }
    report_data = pd.DataFrame(user_report_data, index = [0])
    return report_data

# ==================================================
#                    Patient Data
# ==================================================
user_data = user_report()
st.subheader("Patient Data")
st.write(user_data)
# ==================================================
#                    Model
# ==================================================
rc = RandomForestClassifier()
rc.fit(X_train, y_train)
user_result = rc.predict(user_data)
# ==================================================
#                    Visualization
# ==================================================
st.title("Visualized Patient Data")
# ==================================================
#                    Color function
# ==================================================
if user_result[0] == 0:
    color = 'blue'
else:
    color = 'red'
# ==================================================
#                    Age Vs Pregnancies
# ==================================================
st.header("Pregnancy count Graph (Other VS Yours)")
fig_preg = plt.figure()
ax1 = sns.scatterplot(x = "Age", y = 'Pregnancies', 
    data = df, hue = 'Outcome', palette = "Greens"
)
ax2 = sns.scatterplot(x = user_data["age"], y = user_data['pregnancies'],
    s = 150, color = color)
plt.xticks(np.arange(10, 100, 5))
plt.yticks(np.arange(0,20, 2))
plt.title("0 - Healthy  and 1 is Diabetic")
st.pyplot(fig_preg) 
# ==================================================
#                    Your Report
# ==================================================
st.header("Your Report")
output = ''
if user_result[0] == 0:
    output = "You are healthy"
else:
    output = "You are diabetic please do not eat suger"
    st.warning("Sugar, Sugar, Sugar")
st.title(output)
# st.subheader("Accuracy")
# st.write(str(accuracy_score(y_test, rc.predict(X_test)*100 + "%")))


















# Yet to Explore