from sklearn.linear_model import LinearRegression
import numpy as np

x = np.linspace(0, 1)
y = 3 * x + 4 + np.random.rand() / 100
x = x.reshape(-1, 1)

model = LinearRegression()
model.fit(x, y)

print(model.coef_, "sjhdjkashdjskahdjksahdas")
print(model.intercept_)
print(f'y = {model.coef_[0]} * x + {model.intercept_}')
print(y)
print(x,y)
print("changed by mskmei")
print("x,y")
print('rah')
print(x+y)
print("Hello, my name is 黄曦月")
print ('done')
