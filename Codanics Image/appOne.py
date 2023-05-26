# import Required Libraries
import numpy as np
import pandas as pd
import streamlit as st
import plotly as pt
import matplotlib.pyplot as plt
from explainerdashboard import ExplainerDashboard, ClassifierExplainer
from PIL import Image
st.write("Hello World!!! This is an app to educate you about Wild Life")
image1 = Image.open("tiger.jpg")
st.image(image1)
with Image.open("hassan.jpg") as imHassan:
    imHassan.rotate(0).show()
# a = np.asarray(im)
with Image.open("tiger.jpg") as imTiger:
    imTiger.rotate(0).show()

