import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def graph_capacity():
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

# Graph burn/escapees/crush count (y-axis) over tick count (x-axis) by reading escapees-over-time.txt:
def graph_over_time(file):
    col_names = ["tick_count", "crush", "burn", "escape"]
    df = pd.read_csv(file, sep=" ", names=col_names)

    seconds = df['tick_count'] / 60

    plt.plot(seconds, df['crush'], 'r', label='Number of people crushed')
    plt.plot(seconds, df['burn'], 'b', label='Number of people burnt')
    plt.plot(seconds, df['escape'], 'g', label='Number of escapees')

    plt.ylim(bottom=0)
    plt.xlim([0, seconds.iloc[-1]])
    plt.grid(True, axis='both', which='major')
    plt.xlabel('Time elapsed (s)', fontsize=10)
    plt.ylabel('Number of people', fontsize=10)
    plt.title('Escapees from evacuation situation over time', fontsize=14)
    plt.legend()
    plt.show()


def graph_prop_speed(file):
    col_names = ["speed_1", "speed_2", "prop", "total_count", "t1_crush", "t1_burn", "t1_out", "t2_crush", "t2_burn", "t2_out"]
    df = pd.read_csv(file, sep=" ", names=col_names)

    df['speed_1_count'] = df['total_count'] * df['prop']
    df['speed_2_count'] = df['total_count'] * (1-df['prop'])

    grouped = df.groupby(['prop'])
    df['t1_crush_prop'] = grouped['t1_crush'].transform(np.mean) / df['speed_1_count']
    df['t1_burn_prop'] = grouped['t1_burn'].transform(np.mean) / df['speed_1_count']
    df['t1_out_prop'] = grouped['t1_out'].transform(np.mean) / df['speed_1_count']
    df['t2_crush_prop'] = grouped['t2_crush'].transform(np.mean) / df['speed_2_count']
    df['t2_burn_prop'] = grouped['t2_burn'].transform(np.mean) / df['speed_2_count']
    df['t2_out_prop'] = grouped['t2_out'].transform(np.mean) / df['speed_2_count']
    df = df.drop_duplicates(subset=['prop'])

    no_nan_df = df.fillna(0)

    df['total_crush_prop'] = (no_nan_df['t1_crush_prop'] * df['prop']) + (no_nan_df['t2_crush_prop'] * (1-df['prop']))
    df['total_burn_prop'] = (no_nan_df['t1_burn_prop'] * df['prop']) + (no_nan_df['t2_burn_prop'] * (1-df['prop']))
    df['total_out_prop'] = (no_nan_df['t1_out_prop'] * df['prop']) + (no_nan_df['t2_out_prop'] * (1-df['prop']))

    # fig, ax = plt.subplots()

    x_pop_percent_slow = df['prop']

    y_slow_escape_prop = df['t1_out_prop']
    y_slow_burn_prop = df['t1_burn_prop']
    y_slow_crush_prop = df['t1_crush_prop']

    y_fast_escape_prop = df['t2_out_prop']
    y_fast_burn_prop = df['t2_burn_prop']
    y_fast_crush_prop = df['t2_crush_prop']

    y_total_escape_prop = df['total_out_prop']
    y_total_burn_prop = df['total_burn_prop']
    y_total_crush_prop = df['total_crush_prop']

    plt.plot(x_pop_percent_slow, y_slow_escape_prop, 'r', label='Slow Pop Escaped')
    plt.plot(x_pop_percent_slow, y_slow_burn_prop, 'r--', label='Slow Pop Burned')
    plt.plot(x_pop_percent_slow, y_slow_crush_prop, 'r:', label='Slow Pop Crushed')
    plt.plot(x_pop_percent_slow, y_fast_escape_prop, 'g', label='Fast Pop Escaped')
    plt.plot(x_pop_percent_slow, y_fast_burn_prop, 'g--', label='Fast Pop Burned')
    plt.plot(x_pop_percent_slow, y_fast_crush_prop, 'g:', label='Fast Pop Crushed')
    plt.plot(x_pop_percent_slow, y_total_escape_prop, 'b', label='Total Pop Escaped')
    plt.plot(x_pop_percent_slow, y_total_burn_prop, 'b--', label='Total Pop Burned')
    plt.plot(x_pop_percent_slow, y_total_crush_prop, 'b:', label='Total Pop Crushed')

    plt.ylim([0, 1])
    plt.xlim([0, 1])

    plt.xlabel('Slow Agent Proportion of Total Population', fontsize = 12)
    plt.ylabel('Sub-Population Escape Proportion', fontsize = 12)
    plt.title('Escape Rate by Agent Speed - 1 Door with Chokes', fontsize = 20)
    plt.legend()
    plt.show()



basic = "speed-proportion-real.txt"
twoExits = "speed-prop-2exit-real.txt"
middleFire = "middlefire-real.txt"
door = "door-real.txt"
block_devider = "door-block-real.txt"
doors_4 = "4Doors-real.txt"
choke_4 = '4choke-real.txt'
choke_4_nochoke = '4choke-nochoke-real.txt'
choke_3_fat = '3choke-fat.txt'
choke_4_nochoke_dist = '4choke-nochoke-dist-real.txt'

#Tests since Panic was altered
fire3_4skinnychoke_randomdist_2door = "fire3_4skinnychoke_randomdist_2door.txt"
fire3_randomdist_1door = 'fire3_randomdist_1door.txt'
fire3_nochoke_randomdist_2door = 'fire3-nochoke-randomdist-2door.txt'
fire3_4skinnychoke_randomdist_1door = 'fire3_4skinnychoke_randomdist_1door.txt'
# graph_prop_speed(fire3_4skinnychoke_randomdist_1door)
graph_over_time('escapees-over-time.txt')