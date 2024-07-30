import pandas as pd
import os

# Load the config file
config_path = r'path'
config_df = pd.read_excel(config_path)

# Extract values from the config file
data_set_path = config_df.loc[config_df['Key'] == 'data_set_path', 'Value'].values[0]
output_path = config_df.loc[config_df['Key'] == 'output_path', 'Value'].values[0]
output_file = os.path.join(output_path, 'filtered_data.xlsx')

# Debugging: Print the paths to verify correctness
print(f"Config Path: {config_path}")
print(f"Data Set Path: {data_set_path}")
print(f"Output Path: {output_path}")
print(f"Output File: {output_file}")

# Check if the config file exists
if not os.path.exists(config_path):
    raise FileNotFoundError(f"Config file not found at {config_path}")

# Check if the dataset file exists
if not os.path.exists(data_set_path):
    raise FileNotFoundError(f"Data set file not found at {data_set_path}")

# Ensure the output directory exists
os.makedirs(output_path, exist_ok=True)

# Read the dataset
df = pd.read_csv(data_set_path)

# Filter the rows where 'Competition' column has the value 'eng Premier League'
filtered_df = df[df['Competition'] == 'eng Premier League']

# Write the filtered data to a new Excel file
with pd.ExcelWriter(output_file, mode='w', engine='openpyxl') as writer:
    filtered_df.to_excel(writer, sheet_name='Filtered_Data', index=False)

print("Filtering completed and saved to", output_file)
