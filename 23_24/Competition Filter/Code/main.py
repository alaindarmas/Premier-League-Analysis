import pandas as pd
import os

# Define the base path relative to the script location
base_path = os.path.dirname(os.path.abspath(__file__))

# Construct the relative path to the config file
config_relative_path = os.path.join(base_path, '..', 'Documentation', 'ConfigFile.xlsx')

# Debugging: Print the path to verify correctness
print(f"Config Relative Path: {config_relative_path}")

# Check if the config file exists
if not os.path.exists(config_relative_path):
    raise FileNotFoundError(f"Config file not found at {config_relative_path}")

# Load the config file
config_df = pd.read_excel(config_relative_path)

# Extract values from the config file and convert them to absolute paths
data_set_relative_path = config_df.loc[config_df['Key'] == 'data_set_path', 'Value'].values[0]
output_relative_path = config_df.loc[config_df['Key'] == 'output_path', 'Value'].values[0]

data_set_path = os.path.abspath(os.path.join(base_path, data_set_relative_path))
output_path = os.path.abspath(os.path.join(base_path, output_relative_path))
output_file = os.path.join(output_path, 'filtered_data.xlsx')

# Debugging: Print the constructed paths
print(f"Data Set Path: {data_set_path}")
print(f"Output Path: {output_path}")
print(f"Output File: {output_file}")

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
