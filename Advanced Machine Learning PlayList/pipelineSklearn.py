import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
X,y = load_boston(return_X_y=True)
print(X)
scaler = StandardScaler()
scaled_X = scaler.fit_transform(X)
print(scaled_X)
