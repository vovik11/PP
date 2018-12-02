import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('NYC_Jobs.csv')
df['median'] = df.groupby('Salary Range From')['Salary Range To'].transform(np.median)
gb = df.groupby('Work Location')
df1 = pd.DataFrame([df.loc[gb.groups[n], 'median'].values for n in gb.groups], index=gb.groups.keys())
df1 = df1.median(axis=1)
df1.plot()
plt.show()
