import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#gap_df = pd.read_csv("out_abv1.csv")

#stations = gap_df["station"].unique()
#print(len(stations))
#print(gap_df['gaps'])
#fig, axes = plt.subplots(len(stations), 1, figsize=(8, 16), sharex=True)
#plt.plot(gap_df["gaps"])
#plt.show()


import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("out_abv1.csv")
stat = df['station'].unique()
print(stat)
n = 0
fig, axs = plt.subplots(5,8)
axs = axs.ravel()

for station in stat:
    
    a=df.loc[df['station'] == station]['gaps']

    axs[n].hist(np.log10(a), bins=30, alpha=0.5, color='b')
    axs[n].set_title(station)
    axs[n].set_xlabel('Gap [s]')
    axs[n].set_ylabel('Frequency')

    n+=1
    
    
plt.show()


