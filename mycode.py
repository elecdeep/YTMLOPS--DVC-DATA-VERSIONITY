import pandas as pd 
import os 
# create a sample DataFramewith column names
data = {'Name': ['Alice', 'Bob', 'Charlie'],
       'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)
#Define the file path
file_path=os.path.join(data_dir,'sample_data.csv')

#save the DataFrame to a csv file, including column names
df.to_csv(file_path,index=False)

print(f"csv file saved to {file_path}")
