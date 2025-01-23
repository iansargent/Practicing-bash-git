import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np

df = pd.read_csv('EXAMPLE_REVENUE.csv', delimiter=',', na_values=['NA'])

print(df)

df['Revenue'] = df['Revenue'].replace(',', '', regex=True).astype(float)

# Extract the year and quarter from the 'Quarter' column
def quarter_to_datetime(quarter_str):
    quarter, year = quarter_str.split()
    year = int(year)
    month = {'Q1': '01', 'Q2': '04', 'Q3': '07', 'Q4': '10'}[quarter]
    return f'{year}-{month}-01'

df['Quarter'] = pd.to_datetime(df['Quarter'].apply(quarter_to_datetime))

df = df.set_index('Quarter')

df = df.asfreq('QS')

# Seasonal decomposition
result = seasonal_decompose(df['Revenue'], model='additive')

# Plot the seasonal decomposition
fig, axs = plt.subplots(4, 1, figsize=(12, 10), sharex=True, tight_layout=True)
fig.suptitle('Seasonal Decomposition of Revenue', fontsize=16, fontweight='bold')

# Plot each component with improved styling
components = ['observed', 'trend', 'seasonal', 'resid']
titles = ['Observed', 'Trend', 'Seasonal', 'Residual']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

for i, component in enumerate(components):
    axs[i].plot(result.observed if component == 'observed' else 
                result.trend if component == 'trend' else 
                result.seasonal if component == 'seasonal' else 
                result.resid, color=colors[i], linewidth=2)
    axs[i].set_title(titles[i], fontsize=14, fontweight='bold')
    axs[i].set_ylabel('Value', fontsize=10)
    axs[i].grid(True, linestyle='--', alpha=0.7)
    axs[i].legend([titles[i]], loc='best', fontsize=10)

    axs[i].xaxis.set_major_locator(plt.MaxNLocator(10))  # Increase the number of x-axis gridlines
    axs[i].yaxis.set_major_locator(plt.MaxNLocator(10))  # Increase the number of y-axis gridlines

# Set x-axis label and format
axs[-1].set_xlabel('Date', fontsize=12)
axs[-1].tick_params(axis='x', rotation=45)
plt.xticks(fontsize=10)
plt.yticks(fontsize=8)

# Show the plot
plt.show()
