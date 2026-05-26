# Visualisation Of Iris Dataset.(9Nov)

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
link=link="https://raw.githubusercontent.com/swapnilsaurav/Dataset/refs/heads/master/Iris.csv"
df = pd.read_csv(link)
print(df)
print(df.describe())
import matplotlib.pyplot as plt

# scatter plot
plt.figure()
plt.scatter(df['SepalLengthCm'], df['PetalLengthCm'])
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.title("Sepal Length vs Petal Length")
plt.show()

# histogram
plt.figure()
plt.hist(df['SepalLengthCm'])
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()

