import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

col_names = ["num_exits", "num_agents", "num_ticks"]
df = pd.read_csv("capacity-real.txt", sep=" ", names=col_names)

grouped = df.groupby(['num_exits', 'num_agents'])
df['mean_num_ticks'] = grouped['num_ticks'].transform(np.mean)
df = df.drop_duplicates(subset=['num_exits', 'num_agents'])

num_exits= (list(df.loc[:, 'num_exits']))
num_agents_1 = [str(x) for x in (np.array(df.loc[df['num_exits'] == 1, 'num_agents']))]
num_agents_2 = [str(x) for x in (np.array(df.loc[df['num_exits'] == 2, 'num_agents']))]
mean_num_ticks_1 =(list(df.loc[df['num_exits'] == 1, 'mean_num_ticks']))
mean_num_ticks_2 =(list(df.loc[df['num_exits'] == 2, 'mean_num_ticks']))

fig, ax = plt.subplots()

w=0.4
ax.bar(num_agents_1, mean_num_ticks_1, width=w, color='b', align='edge', label="One Exit")
ax.bar(num_agents_2, mean_num_ticks_2, width=-w, color='g', align='edge', label="Two Exits")
ax.autoscale(tight=True)
ax.set_xticks(num_agents_1)

plt.xlabel('Number of Agents', fontsize = 12)
plt.ylabel('Ticks', fontsize = 12)
plt.title('Escape Time By Agent and Exit Count', fontsize = 20)
plt.legend()
plt.show()



# ax = df.plot.bar(rot=0)