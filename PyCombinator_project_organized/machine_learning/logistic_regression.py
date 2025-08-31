
from sklearn.linear_model import LinearRegression
import numpy as np

def train_model(X, y):
    model = LinearRegression()
    model.fit(X, y)
    return model

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([1, 2, 3, 4, 5])
model = train_model(X, y)

print("Model Coefficients:")
print(model.coef_)
