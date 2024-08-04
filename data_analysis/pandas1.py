import pandas as pd
import matplotlib.pyplot as plt

hour=pd.read_csv("C:\\Users\\rishi\\git\\python\\data_analysis\\hour.csv")
print(hour.head())
print(hour['count'].mean())

def dev(num:int,den:int)-> float:
    return num/den

fig, ax = plt.subplots(figsize=(10, 6))
ax.scatter(x = hour['instant'], y = hour['count'])
plt.show()