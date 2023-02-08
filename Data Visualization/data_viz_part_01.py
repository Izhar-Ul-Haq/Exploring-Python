import numpy as np
import pandas as pd
import sklearn as sk
# Data Vis By Codanics
import seaborn as sns
import matplotlib.pyplot as plt
# import datasets
kashti = sns.load_dataset('titanic')
print(kashti)
print(kashti.info)
print(kashti.isnull().sum())
print(kashti.survived.value_counts().plot(kind = "bar"))
print(sns.countplot(x = "survived", data = kashti))