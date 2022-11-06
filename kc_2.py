import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('assets/california_housing_test.csv')
df.head()

x=df['median_income']
y=df['median_house_value']

plt.scatter(x,y)
plt.show()
