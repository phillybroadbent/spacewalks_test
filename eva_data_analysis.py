import matplotlib.pyplot as plt
import pandas as pd

# https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r',  encoding="utf-8")
output_file = open('./eva-data.csv','w',  encoding="utf-8")
graph_file = './cumulative_eva_graph.png'


print('--START--')
print(f'Reading JSON file {input_file}')
#Read the data from a JSON file into a pandas dataframe
eva_df = pd.read_json(input_file, convert_dates=['date'])
eva_df['eva'] = eva_df['eva'].astype(float)

# Clean the data by removing any incomplete rows and sort by date
eva_df.dropna(axis=0, inplace=True)
eva_df.sort_values('date', inplace=True)

print(f'Saving to CSV file {output_file}')
# Save dataframe to CSV file for later analysis
eva_df.to_csv(output_file, index=False)

print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')
#Plot cumulative time in space over the years
eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()


plt.plot(eva_df['date'],eva_df['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
print('--END')
