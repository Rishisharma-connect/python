import pandas as pd
hour=pd.read_csv("C:\\Users\\rishi\\git\\python\\data_analysis\\hour.csv")
print(hour.head())
print(hour['count'].mean())

def dev(num:int,den:int)-> float:
    return num/den

print(dev()pip3 