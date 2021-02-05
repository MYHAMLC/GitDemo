import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('D:\\Python-workspace\\apple.csv')
# print(data)
x = data.loc[:,'Volume']
plt.plot(x)
plt.show()

