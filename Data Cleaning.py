#!/usr/bin/env python
# coding: utf-8

# In[1]:


"C:\BA\Projects\Business Decision support system\Data\flightlist_20200101_20200131.csv"


# In[3]:


import os
import pandas as pd

# Define the file path of the CSV file
file_path = r"C:\BA\Projects\Business Decision support system\Data\flightlist_20200201_20200229.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Drop rows with missing values
df.dropna(inplace=True)

# Print the cleaned DataFrame
print(df)

# Extract the directory path from the original file path
directory_path = os.path.dirname(file_path)

# Specify the new file name for the cleaned data
output_file_name = 'data_2020_feb.csv'

# Combine the directory path and the new file name
output_file_path = os.path.join(directory_path, output_file_name)

# Save the cleaned DataFrame to a new CSV file in the same directory as the original file
df.to_csv(output_file_path, index=False)

# Confirm the save operation
print("Cleaned data saved to:", output_file_path)


# In[4]:


import os
import pandas as pd

# Define the file path of the CSV file
file_path = r"C:\BA\Projects\Business Decision support system\Data\flightlist_20200301_20200331.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Drop rows with missing values
df.dropna(inplace=True)

# Print the cleaned DataFrame
print(df)

# Extract the directory path from the original file path
directory_path = os.path.dirname(file_path)

# Specify the new file name for the cleaned data
output_file_name = 'data_2020_mar.csv'

# Combine the directory path and the new file name
output_file_path = os.path.join(directory_path, output_file_name)

# Save the cleaned DataFrame to a new CSV file in the same directory as the original file
df.to_csv(output_file_path, index=False)

# Confirm the save operation
print("Cleaned data saved to:", output_file_path)


# In[6]:


import os
import pandas as pd

# Define the file path of the CSV file
file_path = r"C:\BA\Projects\Business Decision support system\Data\flightlist_20200401_20200430.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Drop rows with missing values
df.dropna(inplace=True)

# Print the cleaned DataFrame
print(df)

# Extract the directory path from the original file path
directory_path = os.path.dirname(file_path)

# Specify the new file name for the cleaned data
output_file_name = 'data_2020_apr.csv'

# Combine the directory path and the new file name
output_file_path = os.path.join(directory_path, output_file_name)

# Save the cleaned DataFrame to a new CSV file in the same directory as the original file
df.to_csv(output_file_path, index=False)

# Confirm the save operation
print("Cleaned data saved to:", output_file_path)


# In[7]:


import os
import pandas as pd

# Define the file path of the CSV file
file_path = r"C:\BA\Projects\Business Decision support system\Data\flightlist_20200401_20200430.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Remove missing values from all columns except 'origin' and 'destination'
subset_columns = df.columns.difference(['origin', 'destination'])
df.dropna(subset=subset_columns, inplace=True)

# Print the cleaned DataFrame
print(df)

# Extract the directory path from the original file path
directory_path = os.path.dirname(file_path)

# Specify the new file name for the cleaned data
output_file_name = 'data_2_apr.csv'

# Combine the directory path and the new file name
output_file_path = os.path.join(directory_path, output_file_name)

# Save the cleaned DataFrame to a new CSV file in the same directory as the original file
df.to_csv(output_file_path, index=False)

# Confirm the save operation
print("Cleaned data saved to:", output_file_path)


# In[8]:


import os
import pandas as pd

# Define the file path of the CSV file
file_path = r"C:\BA\Projects\Business Decision support system\Data\flightlist_20200401_20200430.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Drop rows with missing values
df.dropna(inplace=True)
# Convert 'firstseen' and 'lastseen' to datetime
df['firstseen'] = pd.to_datetime(df['firstseen'], utc=True)
df['lastseen'] = pd.to_datetime(df['lastseen'], utc=True)

# Calculate the flight duration
df['flight_duration'] = df['lastseen'] - df['firstseen']

# Optionally, convert the duration to minutes for easier interpretation
df['flight_duration_minutes'] = df['flight_duration'].dt.total_seconds() / 60

# Let's take a look at the modified DataFrame with the new 'flight_duration' and 'flight_duration_minutes' columns
print(df[['callsign', 'firstseen', 'lastseen', 'flight_duration', 'flight_duration_minutes']].head())


# Extract the directory path from the original file path
directory_path = os.path.dirname(file_path)

# Specify the new file name for the cleaned data
output_file_name = 'data_3.csv'

# Combine the directory path and the new file name
output_file_path = os.path.join(directory_path, output_file_name)

# Save the cleaned DataFrame to a new CSV file in the same directory as the original file
df.to_csv(output_file_path, index=False)

# Confirm the save operation
print("Cleaned data saved to:", output_file_path)


# In[2]:


import os
import pandas as pd

# Define the file path of the CSV file
file_path = r"C:\BA\Projects\Business Decision support system\Data\flightlist_20200301_20200331.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Drop rows with missing values
df.dropna(inplace=True)
# Convert 'firstseen' and 'lastseen' to datetime
df['firstseen'] = pd.to_datetime(df['firstseen'], utc=True)
df['lastseen'] = pd.to_datetime(df['lastseen'], utc=True)

# Calculate the flight duration
df['flight_duration'] = df['lastseen'] - df['firstseen']

# Optionally, convert the duration to minutes for easier interpretation
df['flight_duration_minutes'] = df['flight_duration'].dt.total_seconds() / 60

# Let's take a look at the modified DataFrame with the new 'flight_duration' and 'flight_duration_minutes' columns
print(df[['callsign', 'firstseen', 'lastseen', 'flight_duration', 'flight_duration_minutes']].head())


# Extract the directory path from the original file path
directory_path = os.path.dirname(file_path)

# Specify the new file name for the cleaned data
output_file_name = 'data_3_feb.csv'

# Combine the directory path and the new file name
output_file_path = os.path.join(directory_path, output_file_name)

# Save the cleaned DataFrame to a new CSV file in the same directory as the original file
df.to_csv(output_file_path, index=False)

# Confirm the save operation
print("Cleaned data saved to:", output_file_path)


# In[3]:


import os
import pandas as pd

# Define the file path of the CSV file
file_path = r"C:\BA\Projects\Business Decision support system\Data\flightlist_20200301_20200331.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Drop rows with missing values
df.dropna(inplace=True)

# Convert 'firstseen', 'lastseen', and 'day' to datetime
df['firstseen'] = pd.to_datetime(df['firstseen'], utc=True)
df['lastseen'] = pd.to_datetime(df['lastseen'], utc=True)
df['day'] = pd.to_datetime(df['day'], utc=True).dt.date  # Convert to datetime and extract the date

# Calculate the flight duration
df['flight_duration'] = df['lastseen'] - df['firstseen']

# Optionally, convert the duration to minutes for easier interpretation
df['flight_duration_minutes'] = df['flight_duration'].dt.total_seconds() / 60

# Let's take a look at the modified DataFrame with the new 'flight_duration', 'flight_duration_minutes', and adjusted 'day' columns
print(df[['callsign', 'firstseen', 'lastseen', 'day', 'flight_duration', 'flight_duration_minutes']].head())

# Extract the directory path from the original file path
directory_path = os.path.dirname(file_path)

# Specify the new file name for the cleaned data
output_file_name = 'cleaned_flight_data.csv'

# Combine the directory path and the new file name
output_file_path = os.path.join(directory_path, output_file_name)

# Save the cleaned DataFrame to a new CSV file in the same directory as the original file
df.to_csv(output_file_path, index=False)

# Confirm the save operation
print("Cleaned data saved to:", output_file_path)


# In[4]:


import os
import pandas as pd

# Define the file path of the CSV file
file_path = r"C:\BA\Projects\Business Decision support system\Data\flightlist_20200201_20200229.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Drop rows with missing values
df.dropna(inplace=True)

# Convert 'firstseen', 'lastseen', and 'day' to datetime
df['firstseen'] = pd.to_datetime(df['firstseen'], utc=True)
df['lastseen'] = pd.to_datetime(df['lastseen'], utc=True)
df['day'] = pd.to_datetime(df['day'], utc=True).dt.date  # Convert to datetime and extract the date

# Calculate the flight duration
df['flight_duration'] = df['lastseen'] - df['firstseen']

# Optionally, convert the duration to minutes for easier interpretation
df['flight_duration_minutes'] = df['flight_duration'].dt.total_seconds() / 60

# Let's take a look at the modified DataFrame with the new 'flight_duration', 'flight_duration_minutes', and adjusted 'day' columns
print(df[['callsign', 'firstseen', 'lastseen', 'day', 'flight_duration', 'flight_duration_minutes']].head())

# Extract the directory path from the original file path
directory_path = os.path.dirname(file_path)

# Specify the new file name for the cleaned data
output_file_name = 'cleaned_flight_data_feb_2020.csv'

# Combine the directory path and the new file name
output_file_path = os.path.join(directory_path, output_file_name)

# Save the cleaned DataFrame to a new CSV file in the same directory as the original file
df.to_csv(output_file_path, index=False)

# Confirm the save operation
print("Cleaned data saved to:", output_file_path)


# In[1]:


import pandas as pd

# Load the datasets
df_feb = pd.read_csv("C:\BA\Projects\Business Decision support system\Data\cleaned_flight_data_feb_2020.csv")
df_mar = pd.read_csv("C:\BA\Projects\Business Decision support system\Data\cleaned_flight_data_Mar_2020.csv")

# Append the March data to the February data
merged_df = pd.concat([df_feb, df_mar], ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('path_where_you_want_to_save/merged_flight_data_Feb_Mar_2020.csv', index=False)


# In[2]:


import pandas as pd

# Define the base path to your files
base_path = r"C:\BA\Projects\Business Decision support system\Data"

# Load the datasets
df_feb = pd.read_csv(f'{base_path}\\cleaned_flight_data_feb_2020.csv')
df_mar = pd.read_csv(f'{base_path}\\cleaned_flight_data_Mar_2020.csv')

# Append the March data to the February data
merged_df = pd.concat([df_feb, df_mar], ignore_index=True)

# Save the merged DataFrame to a new CSV file in the same directory
merged_df.to_csv(f'{base_path}\\merged_flight_data_Feb_Mar_2020.csv', index=False)

print("The merged dataset has been saved successfully.")


# In[3]:


import os
import pandas as pd

# Define the file path of the CSV file
file_path = r"C:\BA\Projects\Business Decision support system\Data\flightlist_20200401_20200430.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Drop rows with missing values
df.dropna(inplace=True)

# Convert 'firstseen', 'lastseen', and 'day' to datetime
df['firstseen'] = pd.to_datetime(df['firstseen'], utc=True)
df['lastseen'] = pd.to_datetime(df['lastseen'], utc=True)
df['day'] = pd.to_datetime(df['day'], utc=True).dt.date  # Convert to datetime and extract the date

# Calculate the flight duration
df['flight_duration'] = df['lastseen'] - df['firstseen']

# Optionally, convert the duration to minutes for easier interpretation
df['flight_duration_minutes'] = df['flight_duration'].dt.total_seconds() / 60

# Let's take a look at the modified DataFrame with the new 'flight_duration', 'flight_duration_minutes', and adjusted 'day' columns
print(df[['callsign', 'firstseen', 'lastseen', 'day', 'flight_duration', 'flight_duration_minutes']].head())

# Extract the directory path from the original file path
directory_path = os.path.dirname(file_path)

# Specify the new file name for the cleaned data
output_file_name = 'cleaned_flight_data_apr_2020.csv'

# Combine the directory path and the new file name
output_file_path = os.path.join(directory_path, output_file_name)

# Save the cleaned DataFrame to a new CSV file in the same directory as the original file
df.to_csv(output_file_path, index=False)

# Confirm the save operation
print("Cleaned data saved to:", output_file_path)


# In[4]:


import pandas as pd

# Define the base path to your files
base_path = r"C:\BA\Projects\Business Decision support system\Data"

# Load the datasets
df_feb = pd.read_csv(f'{base_path}\\merged_flight_data_Feb_Mar_2020.csv')
df_mar = pd.read_csv(f'{base_path}\\cleaned_flight_data_apr_2020.csv')

# Append the March data to the February data
merged_df = pd.concat([df_feb, df_mar], ignore_index=True)

# Save the merged DataFrame to a new CSV file in the same directory
merged_df.to_csv(f'{base_path}\\merged_flight_data_Feb_Mar_2020.csv', index=False)

print("The merged dataset has been saved successfully.")


# In[5]:


import os
import pandas as pd

# Define the file path of the CSV file
file_path = r"C:\BA\Projects\Business Decision support system\Data\flightlist_20200501_20200531.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Drop rows with missing values
df.dropna(inplace=True)

# Convert 'firstseen', 'lastseen', and 'day' to datetime
df['firstseen'] = pd.to_datetime(df['firstseen'], utc=True)
df['lastseen'] = pd.to_datetime(df['lastseen'], utc=True)
df['day'] = pd.to_datetime(df['day'], utc=True).dt.date  # Convert to datetime and extract the date

# Calculate the flight duration
df['flight_duration'] = df['lastseen'] - df['firstseen']

# Optionally, convert the duration to minutes for easier interpretation
df['flight_duration_minutes'] = df['flight_duration'].dt.total_seconds() / 60

# Let's take a look at the modified DataFrame with the new 'flight_duration', 'flight_duration_minutes', and adjusted 'day' columns
print(df[['callsign', 'firstseen', 'lastseen', 'day', 'flight_duration', 'flight_duration_minutes']].head())

# Extract the directory path from the original file path
directory_path = os.path.dirname(file_path)

# Specify the new file name for the cleaned data
output_file_name = 'cleaned_flight_data_may_2020.csv'

# Combine the directory path and the new file name
output_file_path = os.path.join(directory_path, output_file_name)

# Save the cleaned DataFrame to a new CSV file in the same directory as the original file
df.to_csv(output_file_path, index=False)

# Confirm the save operation
print("Cleaned data saved to:", output_file_path)


# In[7]:


import os
import pandas as pd

# Define the file path of the CSV file
file_path = r"C:\BA\Projects\Business Decision support system\Data\flightlist_20200601_20200630.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Drop rows with missing values
df.dropna(inplace=True)

# Convert 'firstseen', 'lastseen', and 'day' to datetime
df['firstseen'] = pd.to_datetime(df['firstseen'], utc=True)
df['lastseen'] = pd.to_datetime(df['lastseen'], utc=True)
df['day'] = pd.to_datetime(df['day'], utc=True).dt.date  # Convert to datetime and extract the date

# Calculate the flight duration
df['flight_duration'] = df['lastseen'] - df['firstseen']

# Optionally, convert the duration to minutes for easier interpretation
df['flight_duration_minutes'] = df['flight_duration'].dt.total_seconds() / 60

# Let's take a look at the modified DataFrame with the new 'flight_duration', 'flight_duration_minutes', and adjusted 'day' columns
print(df[['callsign', 'firstseen', 'lastseen', 'day', 'flight_duration', 'flight_duration_minutes']].head())

# Extract the directory path from the original file path
directory_path = os.path.dirname(file_path)

# Specify the new file name for the cleaned data
output_file_name = 'cleaned_flight_data_june_2020.csv'

# Combine the directory path and the new file name
output_file_path = os.path.join(directory_path, output_file_name)

# Save the cleaned DataFrame to a new CSV file in the same directory as the original file
df.to_csv(output_file_path, index=False)

# Confirm the save operation
print("Cleaned data saved to:", output_file_path)


# In[8]:


import os
import pandas as pd

# Define the file path of the CSV file
file_path = r"C:\BA\Projects\Business Decision support system\Data\flightlist_20200701_20200731.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Drop rows with missing values
df.dropna(inplace=True)

# Convert 'firstseen', 'lastseen', and 'day' to datetime
df['firstseen'] = pd.to_datetime(df['firstseen'], utc=True)
df['lastseen'] = pd.to_datetime(df['lastseen'], utc=True)
df['day'] = pd.to_datetime(df['day'], utc=True).dt.date  # Convert to datetime and extract the date

# Calculate the flight duration
df['flight_duration'] = df['lastseen'] - df['firstseen']

# Optionally, convert the duration to minutes for easier interpretation
df['flight_duration_minutes'] = df['flight_duration'].dt.total_seconds() / 60

# Let's take a look at the modified DataFrame with the new 'flight_duration', 'flight_duration_minutes', and adjusted 'day' columns
print(df[['callsign', 'firstseen', 'lastseen', 'day', 'flight_duration', 'flight_duration_minutes']].head())

# Extract the directory path from the original file path
directory_path = os.path.dirname(file_path)

# Specify the new file name for the cleaned data
output_file_name = 'cleaned_flight_data_july_2020.csv'

# Combine the directory path and the new file name
output_file_path = os.path.join(directory_path, output_file_name)

# Save the cleaned DataFrame to a new CSV file in the same directory as the original file
df.to_csv(output_file_path, index=False)

# Confirm the save operation
print("Cleaned data saved to:", output_file_path)


# In[9]:


import pandas as pd

# Define the base path to your files
base_path = r"C:\BA\Projects\Business Decision support system\Data"

# Load the datasets
df_jan = pd.read_csv(f'{base_path}\\cleaned_flight_data_may_2020.csv')
df_feb = pd.read_csv(f'{base_path}\\cleaned_flight_data_may_2020.csv')
df_may = pd.read_csv(f'{base_path}\\cleaned_flight_data_may_2020.csv')
df_may = pd.read_csv(f'{base_path}\\cleaned_flight_data_may_2020.csv')
df_may = pd.read_csv(f'{base_path}\\cleaned_flight_data_may_2020.csv')
df_june = pd.read_csv(f'{base_path}\\cleaned_flight_data_june_2020.csv')
df_july = pd.read_csv(f'{base_path}\\cleaned_flight_data_july_2020.csv')

# Append the March data to the February data
merged_df = pd.concat([df_may, df_june, df_july], ignore_index=True)

# Save the merged DataFrame to a new CSV file in the same directory
merged_df.to_csv(f'{base_path}\\merged_flight_data_Feb_Mar_2020.csv', index=False)

print("The merged dataset has been saved successfully.")


# In[10]:


import os
import pandas as pd

# Define the file path of the CSV file
file_path = r"C:\BA\Projects\Business Decision support system\Data\flightlist_20200101_20200131.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Drop rows with missing values
df.dropna(inplace=True)

# Convert 'firstseen', 'lastseen', and 'day' to datetime
df['firstseen'] = pd.to_datetime(df['firstseen'], utc=True)
df['lastseen'] = pd.to_datetime(df['lastseen'], utc=True)
df['day'] = pd.to_datetime(df['day'], utc=True).dt.date  # Convert to datetime and extract the date

# Calculate the flight duration
df['flight_duration'] = df['lastseen'] - df['firstseen']

# Optionally, convert the duration to minutes for easier interpretation
df['flight_duration_minutes'] = df['flight_duration'].dt.total_seconds() / 60

# Let's take a look at the modified DataFrame with the new 'flight_duration', 'flight_duration_minutes', and adjusted 'day' columns
print(df[['callsign', 'firstseen', 'lastseen', 'day', 'flight_duration', 'flight_duration_minutes']].head())

# Extract the directory path from the original file path
directory_path = os.path.dirname(file_path)

# Specify the new file name for the cleaned data
output_file_name = 'cleaned_flight_data_jan_2020.csv'

# Combine the directory path and the new file name
output_file_path = os.path.join(directory_path, output_file_name)

# Save the cleaned DataFrame to a new CSV file in the same directory as the original file
df.to_csv(output_file_path, index=False)

# Confirm the save operation
print("Cleaned data saved to:", output_file_path)


# In[13]:


import pandas as pd

# Define the base path to your files
base_path = r"C:\BA\Projects\Business Decision support system\Data"

# Load the datasets
df_jan = pd.read_csv(f'{base_path}\\cleaned_flight_data_jan_2020.csv')
df_feb = pd.read_csv(f'{base_path}\\cleaned_flight_data_feb_2020.csv')
df_mar = pd.read_csv(f'{base_path}\\cleaned_flight_data_mar_2020.csv')
df_apr = pd.read_csv(f'{base_path}\\cleaned_flight_data_apr_2020.csv')
df_may = pd.read_csv(f'{base_path}\\cleaned_flight_data_may_2020.csv')
df_june = pd.read_csv(f'{base_path}\\cleaned_flight_data_june_2020.csv')
df_july = pd.read_csv(f'{base_path}\\cleaned_flight_data_july_2020.csv')

# Append the March data to the February data
merged_df = pd.concat([df_jan, df_feb, df_mar, df_apr, df_may, df_june, df_july], ignore_index=True)

# Save the merged DataFrame to a new CSV file in the same directory
merged_df.to_csv(f'{base_path}\\merged_flight_data_2020.csv', index=False)

print("The merged dataset has been saved successfully.")


# In[15]:


import pandas as pd

# Load the April data
df_april = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\data_3_apr.csv")

# Load the airports data
df_airports = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\airports.csv")

# Adjusting column references according to your file structure
# Mapping origin locations
origin_mapping = df_airports.set_index('IATA Code')['municipality'].to_dict()
df_april['origin_location'] = df_april['origin'].map(origin_mapping)

# Mapping destination locations
destination_mapping = df_airports.set_index('IATA Code')['municipality'].to_dict()
df_april['destination_location'] = df_april['destination'].map(destination_mapping)

# Optionally, inspect the first few rows to verify the mappings
print(df_april.head())

# If everything looks good, you can save this DataFrame to a new file
df_april.to_csv(r"C:\BA\Projects\Business Decision support system\Data\updated_april_data_with_locations.csv", index=False)


# In[16]:


import pandas as pd

# Load the April data
df_april = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\data_3_apr.csv")

# Load the airports data
df_airports = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\airports.csv")

# Adjusting column references according to your file structure
# Mapping origin locations
origin_mapping = df_airports.set_index('IATA Code')['municipality'].to_dict()
df_april['origin_location'] = df_april['origin'].map(origin_mapping)

# Mapping destination locations
destination_mapping = df_airports.set_index('IATA Code')['municipality'].to_dict()
df_april['destination_location'] = df_april['destination'].map(destination_mapping)

# Drop rows where either 'origin_location' or 'destination_location' is NaN
df_april = df_april.dropna(subset=['origin_location', 'destination_location'])

# Optionally, inspect the first few rows to verify the mappings and the drop
print(df_april.head())

# Save the cleaned and updated DataFrame to a new file
df_april.to_csv(r"C:\BA\Projects\Business Decision support system\Data\updated_april_data_with_locations.csv", index=False)


# In[18]:


import pandas as pd

# Load the April data
df_april = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\merged_flight_data_2020.csv")

# Load the airports data
df_airports = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\airports.csv")

# Adjusting column references according to your file structure
# Mapping origin locations
origin_mapping = df_airports.set_index('IATA Code')['municipality'].to_dict()
df_april['origin_location'] = df_april['origin'].map(origin_mapping)

# Mapping destination locations
destination_mapping = df_airports.set_index('IATA Code')['municipality'].to_dict()
df_april['destination_location'] = df_april['destination'].map(destination_mapping)

# Drop rows where either 'origin_location' or 'destination_location' is NaN
df_april = df_april.dropna(subset=['origin_location', 'destination_location'])

# Optionally, inspect the first few rows to verify the mappings and the drop
print(df_april.head())

# Save the cleaned and updated DataFrame to a new file
df_april.to_csv(r"C:\BA\Projects\Business Decision support system\Data\updated_data_with_locations.csv", index=False)


# In[19]:


import os
import pandas as pd

# Define the file path of the CSV file
file_path = r"C:\BA\Projects\Business Decision support system\Data\flightlist_20200801_20200831.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Drop rows with missing values
df.dropna(inplace=True)

# Convert 'firstseen', 'lastseen', and 'day' to datetime
df['firstseen'] = pd.to_datetime(df['firstseen'], utc=True)
df['lastseen'] = pd.to_datetime(df['lastseen'], utc=True)
df['day'] = pd.to_datetime(df['day'], utc=True).dt.date  # Convert to datetime and extract the date

# Calculate the flight duration
df['flight_duration'] = df['lastseen'] - df['firstseen']

# Optionally, convert the duration to minutes for easier interpretation
df['flight_duration_minutes'] = df['flight_duration'].dt.total_seconds() / 60

# Let's take a look at the modified DataFrame with the new 'flight_duration', 'flight_duration_minutes', and adjusted 'day' columns
print(df[['callsign', 'firstseen', 'lastseen', 'day', 'flight_duration', 'flight_duration_minutes']].head())

# Extract the directory path from the original file path
directory_path = os.path.dirname(file_path)

# Specify the new file name for the cleaned data
output_file_name = 'cleaned_flight_data_aug_2020.csv'

# Combine the directory path and the new file name
output_file_path = os.path.join(directory_path, output_file_name)

# Save the cleaned DataFrame to a new CSV file in the same directory as the original file
df.to_csv(output_file_path, index=False)

# Confirm the save operation
print("Cleaned data saved to:", output_file_path)


# In[20]:


import os
import pandas as pd

# Define the file path of the CSV file
file_path = r"C:\BA\Projects\Business Decision support system\Data\flightlist_20200901_20200930.csv"
# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Drop rows with missing values
df.dropna(inplace=True)

# Convert 'firstseen', 'lastseen', and 'day' to datetime
df['firstseen'] = pd.to_datetime(df['firstseen'], utc=True)
df['lastseen'] = pd.to_datetime(df['lastseen'], utc=True)
df['day'] = pd.to_datetime(df['day'], utc=True).dt.date  # Convert to datetime and extract the date

# Calculate the flight duration
df['flight_duration'] = df['lastseen'] - df['firstseen']

# Optionally, convert the duration to minutes for easier interpretation
df['flight_duration_minutes'] = df['flight_duration'].dt.total_seconds() / 60

# Let's take a look at the modified DataFrame with the new 'flight_duration', 'flight_duration_minutes', and adjusted 'day' columns
print(df[['callsign', 'firstseen', 'lastseen', 'day', 'flight_duration', 'flight_duration_minutes']].head())

# Extract the directory path from the original file path
directory_path = os.path.dirname(file_path)

# Specify the new file name for the cleaned data
output_file_name = 'cleaned_flight_data_sep_2020.csv'

# Combine the directory path and the new file name
output_file_path = os.path.join(directory_path, output_file_name)

# Save the cleaned DataFrame to a new CSV file in the same directory as the original file
df.to_csv(output_file_path, index=False)

# Confirm the save operation
print("Cleaned data saved to:", output_file_path)


# In[21]:


import os
import pandas as pd

# Define the file path of the CSV file
file_path = r"C:\BA\Projects\Business Decision support system\Data\flightlist_20201001_20201031.csv"
# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Drop rows with missing values
df.dropna(inplace=True)

# Convert 'firstseen', 'lastseen', and 'day' to datetime
df['firstseen'] = pd.to_datetime(df['firstseen'], utc=True)
df['lastseen'] = pd.to_datetime(df['lastseen'], utc=True)
df['day'] = pd.to_datetime(df['day'], utc=True).dt.date  # Convert to datetime and extract the date

# Calculate the flight duration
df['flight_duration'] = df['lastseen'] - df['firstseen']

# Optionally, convert the duration to minutes for easier interpretation
df['flight_duration_minutes'] = df['flight_duration'].dt.total_seconds() / 60

# Let's take a look at the modified DataFrame with the new 'flight_duration', 'flight_duration_minutes', and adjusted 'day' columns
print(df[['callsign', 'firstseen', 'lastseen', 'day', 'flight_duration', 'flight_duration_minutes']].head())

# Extract the directory path from the original file path
directory_path = os.path.dirname(file_path)

# Specify the new file name for the cleaned data
output_file_name = 'cleaned_flight_data_oct_2020.csv'

# Combine the directory path and the new file name
output_file_path = os.path.join(directory_path, output_file_name)

# Save the cleaned DataFrame to a new CSV file in the same directory as the original file
df.to_csv(output_file_path, index=False)

# Confirm the save operation
print("Cleaned data saved to:", output_file_path)


# In[22]:


import os
import pandas as pd

# Define the file path of the CSV file
file_path = r"C:\BA\Projects\Business Decision support system\Data\flightlist_20201101_20201130.csv"
# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Drop rows with missing values
df.dropna(inplace=True)

# Convert 'firstseen', 'lastseen', and 'day' to datetime
df['firstseen'] = pd.to_datetime(df['firstseen'], utc=True)
df['lastseen'] = pd.to_datetime(df['lastseen'], utc=True)
df['day'] = pd.to_datetime(df['day'], utc=True).dt.date  # Convert to datetime and extract the date

# Calculate the flight duration
df['flight_duration'] = df['lastseen'] - df['firstseen']

# Optionally, convert the duration to minutes for easier interpretation
df['flight_duration_minutes'] = df['flight_duration'].dt.total_seconds() / 60

# Let's take a look at the modified DataFrame with the new 'flight_duration', 'flight_duration_minutes', and adjusted 'day' columns
print(df[['callsign', 'firstseen', 'lastseen', 'day', 'flight_duration', 'flight_duration_minutes']].head())

# Extract the directory path from the original file path
directory_path = os.path.dirname(file_path)

# Specify the new file name for the cleaned data
output_file_name = 'cleaned_flight_data_nov_2020.csv'

# Combine the directory path and the new file name
output_file_path = os.path.join(directory_path, output_file_name)

# Save the cleaned DataFrame to a new CSV file in the same directory as the original file
df.to_csv(output_file_path, index=False)

# Confirm the save operation
print("Cleaned data saved to:", output_file_path)


# In[23]:


import os
import pandas as pd

# Define the file path of the CSV file
file_path = r"C:\BA\Projects\Business Decision support system\Data\flightlist_20201201_20201231.csv"
# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Drop rows with missing values
df.dropna(inplace=True)

# Convert 'firstseen', 'lastseen', and 'day' to datetime
df['firstseen'] = pd.to_datetime(df['firstseen'], utc=True)
df['lastseen'] = pd.to_datetime(df['lastseen'], utc=True)
df['day'] = pd.to_datetime(df['day'], utc=True).dt.date  # Convert to datetime and extract the date

# Calculate the flight duration
df['flight_duration'] = df['lastseen'] - df['firstseen']

# Optionally, convert the duration to minutes for easier interpretation
df['flight_duration_minutes'] = df['flight_duration'].dt.total_seconds() / 60

# Let's take a look at the modified DataFrame with the new 'flight_duration', 'flight_duration_minutes', and adjusted 'day' columns
print(df[['callsign', 'firstseen', 'lastseen', 'day', 'flight_duration', 'flight_duration_minutes']].head())

# Extract the directory path from the original file path
directory_path = os.path.dirname(file_path)

# Specify the new file name for the cleaned data
output_file_name = 'cleaned_flight_data_dec_2020.csv'

# Combine the directory path and the new file name
output_file_path = os.path.join(directory_path, output_file_name)

# Save the cleaned DataFrame to a new CSV file in the same directory as the original file
df.to_csv(output_file_path, index=False)

# Confirm the save operation
print("Cleaned data saved to:", output_file_path)


# In[24]:


import pandas as pd

# Define the base path to your files
base_path = r"C:\BA\Projects\Business Decision support system\Data"

# Load the datasets
df_jan = pd.read_csv(f'{base_path}\\cleaned_flight_data_jan_2020.csv')
df_feb = pd.read_csv(f'{base_path}\\cleaned_flight_data_feb_2020.csv')
df_mar = pd.read_csv(f'{base_path}\\cleaned_flight_data_mar_2020.csv')
df_apr = pd.read_csv(f'{base_path}\\cleaned_flight_data_apr_2020.csv')
df_may = pd.read_csv(f'{base_path}\\cleaned_flight_data_may_2020.csv')
df_june = pd.read_csv(f'{base_path}\\cleaned_flight_data_june_2020.csv')
df_july = pd.read_csv(f'{base_path}\\cleaned_flight_data_july_2020.csv')
df_aug = pd.read_csv(f'{base_path}\\cleaned_flight_data_aug_2020.csv')
df_sep = pd.read_csv(f'{base_path}\\cleaned_flight_data_sep_2020.csv')
df_oct = pd.read_csv(f'{base_path}\\cleaned_flight_data_oct_2020.csv')
df_nov = pd.read_csv(f'{base_path}\\cleaned_flight_data_nov_2020.csv')
df_dec = pd.read_csv(f'{base_path}\\cleaned_flight_data_dec_2020.csv')

# Append the March data to the February data
merged_df = pd.concat([df_jan, df_feb, df_mar, df_apr, df_may, df_june, df_july, df_aug, df_sep, df_oct, df_nov, df_dec], ignore_index=True)

# Save the merged DataFrame to a new CSV file in the same directory
merged_df.to_csv(f'{base_path}\\merged_flight_data_year_2020.csv', index=False)

print("The merged dataset has been saved successfully.")


# In[25]:


import pandas as pd

# Load the April data
df_april = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\merged_flight_data_year_2020.csv")

# Load the airports data
df_airports = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\airports.csv")

# Adjusting column references according to your file structure
# Mapping origin locations
origin_mapping = df_airports.set_index('IATA Code')['municipality'].to_dict()
df_april['origin_location'] = df_april['origin'].map(origin_mapping)

# Mapping destination locations
destination_mapping = df_airports.set_index('IATA Code')['municipality'].to_dict()
df_april['destination_location'] = df_april['destination'].map(destination_mapping)

# Drop rows where either 'origin_location' or 'destination_location' is NaN
df_april = df_april.dropna(subset=['origin_location', 'destination_location'])

# Optionally, inspect the first few rows to verify the mappings and the drop
print(df_april.head())

# Save the cleaned and updated DataFrame to a new file
df_april.to_csv(r"C:\BA\Projects\Business Decision support system\Data\updated_data_with_locations_2020.csv", index=False)


# In[27]:


import pandas as pd

# Paths to your files
april_data_path = r"C:\BA\Projects\Business Decision support system\Data\merged_flight_data_year_2020.csv"
airports_data_path = r"C:\BA\Projects\Business Decision support system\Data\airports.csv"
output_path = r"C:\BA\Projects\Business Decision support system\Data\updated_data_with_locations_2020.csv"

# Load the data
df_april = pd.read_csv(april_data_path)
df_airports = pd.read_csv(airports_data_path)

# Creating mappings
origin_mapping = df_airports.set_index('IATA Code')['municipality'].to_dict()
destination_mapping = df_airports.set_index('IATA Code')['municipality'].to_dict()

# Apply mappings
df_april['origin_location'] = df_april['origin'].map(origin_mapping)
df_april['destination_location'] = df_april['destination'].map(destination_mapping)

# Drop rows with NaN in newly created columns
df_april.dropna(subset=['origin_location', 'destination_location'], inplace=True)

# Save the updated DataFrame
df_april.to_csv(output_path, index=False)


# In[29]:


import pandas as pd

# Path to your original dataset
data_path = r"C:\BA\Projects\Business Decision support system\Data\updated_data_with_locations_2020.csv"

# Load the dataset
df = pd.read_csv(data_path)

# Drop the 'icao24' and 'registration' columns
df.drop(columns=['icao24', 'registration','altitude_1', 'altitude_2', 'firstseen', 'lastseen', 'aircraft_uid'], inplace=True)

# Specify the path where you want to save the cleaned dataset
output_path = r"C:\BA\Projects\Business Decision support system\Data\cleaned_data_2020.csv"

# Save the cleaned dataframe to a new CSV file
df.to_csv(output_path, index=False)


# In[3]:


import pandas as pd

# Load your dataset
airlines_data = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\draft\airlines.csv")

# Columns to drop
columns_to_drop = ['Alias', 'IATA', 'Active', 'Callsign', 'Airline ID']

# Dropping the specified columns
airlines_data_cleaned = airlines_data.drop(columns=columns_to_drop, errors='ignore')

# Dropping rows with missing values
airlines_data_cleaned_no_na = airlines_data_cleaned.dropna()

# Saving the cleaned DataFrame to a new CSV file
airlines_data_cleaned_no_na.to_csv(r"C:\BA\Projects\Business Decision support system\Data\draft\cleaned_airlines.csv", index=False)


# In[4]:


import pandas as pd

# Load your dataset
airlines_data = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\draft\Draft cleaned_data_2020.csv")

# Columns to drop
columns_to_drop = ['Alias', 'IATA', 'Active', 'Callsign', 'Airline ID']

# Dropping the specified columns
airlines_data_cleaned = airlines_data.drop(columns=columns_to_drop, errors='ignore')

# Dropping rows with missing values
airlines_data_cleaned_no_na = airlines_data_cleaned.dropna()

# Saving the cleaned DataFrame to a new CSV file
airlines_data_cleaned_no_na.to_csv(r"C:\BA\Projects\Business Decision support system\Data\draft\draft_1_clean.csv", index=False)


# In[5]:


import pandas as pd

# Load your dataset
file_path = r"C:\BA\Projects\Business Decision support system\Data\draft\Draft cleaned_data_2020.csv"
airlines_data = pd.read_csv(file_path)

# Columns to drop
columns_to_drop = ['flight_duration', 'flight_duration_minutes']

# Dropping the specified columns
airlines_data_cleaned = airlines_data.drop(columns=columns_to_drop, errors='ignore')

# Dropping rows with missing values
airlines_data_cleaned_no_na = airlines_data_cleaned.dropna()

# Saving the cleaned DataFrame back to the original file, overwriting it
airlines_data_cleaned_no_na.to_csv(file_path, index=False)


# In[ ]:


import pandas as pd

# Load the first CSV file
df1 = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\draft\Draft cleaned_data_2020.csv")

# Load the second CSV file
df2 = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\draft\cleaned_airlines.csv")

# Extract the first three characters from the call sign in the first file
df1['ICAO_prefix'] = df1['callsign'].str[:3]

# Merge the dataframes based on the extracted ICAO prefix
merged_df = pd.merge(df1, df2, left_on='ICAO_prefix', right_on='ICAO', how='left')

# Select only the necessary columns (e.g., call sign and airline name)
mapped_data = merged_df[['callsign', 'name']]

# Drop rows with missing values (NaN)
mapped_data = mapped_data.dropna()

# Save the mapped data to a new Excel file in the same directory
mapped_data.to_excel(r"C:\BA\Projects\Business Decision support system\Data\draft\mapped_data.xlsx", index=False)


# In[8]:


import pandas as pd

# Load the first CSV file
df1 = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\draft\Draft cleaned_data_2020.csv")

# Load the second CSV file
df2 = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\draft\cleaned_airlines.csv")

# Extract the first three characters from the call sign in the first file
df1['ICAO_prefix'] = df1['callsign'].str[:3]

# Merge the dataframes based on the extracted ICAO prefix
merged_df = pd.merge(df1, df2, left_on='ICAO_prefix', right_on='ICAO', how='left')

# Select only the necessary columns (e.g., call sign and airline name)
mapped_data = merged_df[['callsign', 'Name']]

# Drop rows with missing values (NaN)
mapped_data = mapped_data.dropna()

# Save the mapped data to a new CSV file in the same directory
mapped_data.to_csv(r"C:\BA\Projects\Business Decision support system\Data\draft\mapped_data.csv", index=False)


# In[10]:


import pandas as pd

# Load the first CSV file
df1 = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\draft\Draft cleaned_data_2020.csv")

# Load the second CSV file
df2 = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\draft\cleaned_airlines.csv")

# Extract the first three characters from the call sign in the first file
df1['ICAO_prefix'] = df1['callsign'].str[:3]

# Merge the dataframes based on the extracted ICAO prefix
merged_df = pd.merge(df1, df2, left_on='ICAO_prefix', right_on='ICAO', how='left')

# Drop unnecessary columns
merged_df.drop(['ICAO', 'ICAO_prefix'], axis=1, inplace=True)

# Drop rows with missing values (NaN)
merged_df = merged_df.dropna()

# Save the updated dataframe back to the same CSV file
merged_df.to_csv(r"C:\BA\Projects\Business Decision support system\Data\draft\Draft cleaned_data_2020.csv", index=False)


# In[12]:


import pandas as pd

# Load the first CSV file
df1 = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\draft\Draft cleaned_data_2020.csv")

# Load the second CSV file
df2 = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\draft\cleaned_airlines.csv")

# Extract the first three characters from the call sign in the first file
df1['ICAO_prefix'] = df1['callsign'].str[:3]

# Merge the dataframes based on the extracted ICAO prefix
merged_df = pd.merge(df1, df2, left_on='ICAO_prefix', right_on='ICAO', how='left')

# Drop unnecessary columns
merged_df.drop(['ICAO', 'ICAO_prefix'], axis=1, inplace=True)

# Drop rows with missing values (NaN)
merged_df = merged_df.dropna()

# Rename the column containing the airline names to 'airline_name'
merged_df = merged_df.rename(columns={'Name': 'airline_name'})

# Rearrange columns
mapped_data = merged_df[['callsign', 'airline_name'] + [col for col in merged_df.columns if col not in ['callsign', 'airline_name']]]

# Save the updated dataframe back to the same CSV file
mapped_data.to_csv(r"C:\BA\Projects\Business Decision support system\Data\draft\Draft cleaned_data_2020.csv", index=False)


# In[16]:


import pandas as pd

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(r"C:\BA\Projects\Business Decision support system\Data\draft\Draft cleaned_data_2020.csv")  # Replace 'your_excel_file.xlsx' with your actual file path

# Add a new column named 'Row_id' with row numbers starting from 1
df['Row_id'] = df.index + 1

# Save the modified DataFrame back to the same Excel file (in-place modification)
df = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\draft\Draft cleaned_data_2020.csv")
  # Replace 'your_excel_file.xlsx' with your actual file path

# Print the DataFrame (optional)
print(df)


# In[19]:


import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(r"C:\BA\Projects\Business Decision support system\Data\draft\Draft cleaned_data_2020.csv")

# Add a new column named 'Row_id' with row numbers starting from 1
df['Row_id'] = df.index + 1

# Create a new filename with a descriptive name (optional)
new_filename = "Draft_cleaned_data_2020_with_Row_id.csv"  # Replace with your desired name

# Save the modified DataFrame to a new CSV file in the same directory
df.to_csv(new_filename, index=False)

# Print the DataFrame (optional)
print(df)


# In[20]:


import pandas as pd
import os

# Original file path
original_file_path = r"C:\BA\Projects\Business Decision support system\Data\draft\Draft cleaned_data_2020.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(original_file_path)

# Add a new column named 'Row_id' with row numbers starting from 1
df['Row_id'] = df.index + 1

# Create a new filename with a descriptive name (optional)
new_filename = "Draft_cleaned_data_2020_with_Row_id.csv"

# Construct the full path for the new file, ensuring it's saved in the same directory as the original
new_file_path = os.path.join(os.path.dirname(original_file_path), new_filename)

# Save the modified DataFrame to a new CSV file in the same directory as the original file
df.to_csv(new_file_path, index=False)

# Print the DataFrame (optional)
print(df)


# In[1]:


import pandas as pd
import os

# Load the dataset
file_path = r"C:\BA\Projects\Business Decision support system\Data\data_3_apr.csv"  # Use a raw string
flights_data = pd.read_csv(file_path)

# Create a route identifier
flights_data['route'] = flights_data['origin'] + '-' + flights_data['destination']

# Derive the new file path in the same directory
directory = os.path.dirname(file_path)
new_file_name = "updated_data_with_routes.csv"
new_file_path = os.path.join(directory, new_file_name)

# Save the updated DataFrame to the new file
flights_data.to_csv(new_file_path, index=False)

print(f"Updated dataset saved to: {new_file_path}")


# In[2]:


import pandas as pd

# Correcting the file paths using raw strings
file_path = r"C:\BA\Projects\Business Decision support system\Data\draft\Draft_cleaned_data_2020_with_Row_id.csv"

# Load the dataset
flights_data = pd.read_csv(file_path)

# Drop the 'Row_id' column
flights_data = flights_data.drop(columns=['Row_id'])

# Optionally, create a 'route' column for analysis
flights_data['route'] = flights_data['origin_location'] + '-' + flights_data['destination_location']

# Save the updated DataFrame back to a CSV file, creating a new one
new_file_path = r"C:\BA\Projects\Business Decision support system\Data\draft\updated_data_without_Row_id.csv"
flights_data.to_csv(new_file_path, index=False)

print(f"Updated dataset saved to: {new_file_path}")


# In[5]:


import pandas as pd
import os

# Path to the main dataset
main_file_path = r"C:\BA\Projects\Business Decision support system\Data\draft\updated_data_without_Row_id.csv"
# Load the main dataset
main_df = pd.read_csv(main_file_path)

# Normalize 'callsign' in the main dataset
main_df['callsign'] = main_df['callsign'].str.strip().str.upper()

# Path to the second dataset that includes the flight_duration_minutes column
second_file_path = r"C:\BA\Projects\Business Decision support system\Data\flight_duration_minutes.csv"
# Load the second dataset
second_df = pd.read_csv(second_file_path)

# Normalize 'callsign' in the second dataset
second_df['callsign'] = second_df['callsign'].str.strip().str.upper()

# Merge the main dataset with the relevant column from the second dataset
# Using 'left' join to keep everything from the main dataset and add matching entries from the second dataset
merged_df = pd.merge(main_df, second_df[['callsign', 'flight_duration_minutes']], on='callsign', how='left')

# Derive the output file path in the same directory as the main file
output_file_path = os.path.join(os.path.dirname(main_file_path), 'updated_main_file.csv')

# Save the merged DataFrame to a new CSV file in the same directory as the main file
merged_df.to_csv(output_file_path, index=False)

# Print the first few rows of the merged DataFrame to verify
print(merged_df.head())


# In[6]:


import pandas as pd

# Load the dataset
data_path = r"C:\BA\Projects\Business Decision support system\Data\full_data_covid.csv"  # Windows path format
covid_data = pd.read_csv(data_path)

# Convert the 'date' column to datetime
covid_data['date'] = pd.to_datetime(covid_data['date'])

# Set the date column as the index for resampling
covid_data.set_index('date', inplace=True)

# Resample and sum new cases monthly across all locations
monthly_new_cases = covid_data['new_cases'].resample('M').sum()

# Reset the index to turn the date index back into a column
monthly_new_cases = monthly_new_cases.reset_index()

# Print the aggregated monthly data to verify
print(monthly_new_cases)

# Optionally save the results to a CSV file for further analysis or reporting
output_file_path = r"C:\BA\Projects\Business Decision support system\Data\monthly_new_cases_global.csv"  # Keep consistent Windows path
monthly_new_cases.to_csv(output_file_path, index=False)

print(f"Aggregated monthly new cases saved to: {output_file_path}")


# In[7]:


import pandas as pd

# Load the dataset
data_path = r"C:\BA\Projects\Business Decision Support System\Data\full_data_covid.csv"  # Ensure this path is correct
covid_data = pd.read_csv(data_path)

# Convert the 'date' column to datetime
covid_data['date'] = pd.to_datetime(covid_data['date'])

# Filter the data for the year 2020
covid_data = covid_data[covid_data['date'].dt.year == 2020]

# Set the date column as the index for resampling
covid_data.set_index('date', inplace=True)

# Resample and sum new cases monthly across all locations
monthly_new_cases = covid_data['new_cases'].resample('M').sum()

# Reset the index to turn the date index back into a column
monthly_new_cases = monthly_new_cases.reset_index()

# Change the date format to month names
monthly_new_cases['date'] = monthly_new_cases['date'].dt.strftime('%B')

# Print the aggregated monthly data to verify
print(monthly_new_cases)

# Optionally save the results to a CSV file for further analysis or reporting
output_file_path = r"C:\BA\Projects\Business Decision Support System\Data\monthly_new_cases_2020.csv"  # Adjust the path as needed
monthly_new_cases.to_csv(output_file_path, index=False)

print(f"Aggregated monthly new cases for 2020 saved to: {output_file_path}")


# In[8]:


import pandas as pd
import os

# Paths to your files
main_file_path = r"C:\BA\Projects\Business Decision support system\Data\draft\updated_data_without_Row_id.csv"
second_file_path = r"C:\BA\Projects\Business Decision support system\Data\Updated_airports.csv"

# Load the data
main_df = pd.read_csv(main_file_path)
second_df = pd.read_csv(second_file_path)

# Rename 'ident' to 'origin' and 'name' to 'airport_name' in the second DataFrame
second_df.rename(columns={'ident': 'origin', 'name': 'airport_name'}, inplace=True)

# Merge the DataFrames on 'origin' column
merged_df = pd.merge(main_df, second_df[['origin', 'airport_name']], on='origin', how='left')

# Derive the output file path in the same directory as the main file
output_file_path = os.path.join(os.path.dirname(main_file_path), 'merged_file.csv')

# Save the merged DataFrame
merged_df.to_csv(output_file_path, index=False)

# Print the first few rows of the merged DataFrame to verify
print(merged_df.head())

# Confirmation message
print(f"Merged data saved to: {output_file_path}")


# In[ ]:




