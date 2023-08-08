# Crunchy v.1.005
#
# object based file reading program
# aka I am sick of rewriting the same code
# written to handle small to large data sets
# can convert csv to bin and bin to csv
# compiles csvs into dictionaries for parsing
# uses pandas to handle medium data sets
# dask for large ones
# for large data sets: Parallel processing set at 3.007 gb of RAM

# by. G. Alex Trimble


import numpy as np
import csv
import pickle
import os
import pandas as pd



class Crunchy:
    def __init__(self,filename):
        self.filename = filename
        self.type = ''
    def getFile(self):
        return self.filename

    def getType(self):
        self.type = self.filename[-4:]
        return self.type
    def file_exists(self):
        if not os.path.exists(self.filename):
            raise FileNotFoundError("The specified file does not exist")
class CrunchyCSV(Crunchy):
    def __init__(self,filename,orientation):
        super().__init__(filename)
        self.orientation = orientation

    def DetermineOrient(self):

        with open(self.filename,'r') as csv_file:
            reader = csv.reader(csv_file)
            header = next(reader)
        if self.orientation not in header:
            raise ValueError("Invalid orientation.The specified column does not exist.")
        return self.orientation

    def compile_dict(self,data_type='csv'):
        data_dict = {}
        if data_type =='csv':
            with open(self.filename,'r') as csv_file:
                reader = csv.DictReader(csv_file)
                for row in reader:
                    key = row[self.orientation]
                    data_dict[key] = row
        elif data_type =='numpy':
            data = np.getfromtext(self.filename,delimiter=',',names=True,dtype=None)
            for row in data:
                key = row[self.orientation]
                data_dict[key] = row.tolist()
        else:
            raise ValueError("Invalid data type. Supported options: csv, numpy")
        return data_dict

    def find(self,keywords):
        data_dict = self.compile_dict(data_type='dict')
        keyword_positions = {keyword: [] for keyword in keywords}

        for key, row in data_dict.items():
            for keyword in keywords:
                for column_name, value in row.items():
                    str_value = str(value)  # Convert the value to a string
                    if keyword.lower() in str_value.lower():
                        keyword_positions[keyword].append((key, column_name))

        return keyword_positions

class CrunchyBin(CrunchyCSV):
    def __init__(self,filename):
        super().__init__(filename,orientation=None)


    def load_data(self):
        # Load data from the binary file using pickle
        with open(self.filename, 'rb') as bin_file:
            data = pickle.load(bin_file)
        return data

    def Convert(self, file_type='csv',data_type ='list'):
        if file_type not in ['csv', 'binary']:
            raise ValueError("Invalid file type. Supported options: csv, binary")
        if data_type not in ['list','dict']:
            raise ValueError("Invalid Data type. Supported options: list, dict ")
        if file_type == 'csv':
            # Load data from the binary file
            data = self.load_data()

                # Write the data to a CSV file
            with open(self.filename + '.csv', 'w', newline='') as csv_file:
                if data_type == 'list':
                    writer = csv.writer(csv_file)
                    # Assuming data is a list of lists or a list of tuples                        writer.writerows(data)
                elif data_type == 'dict':
                    writer = csv.DictWriter(csv_file, fieldnames=['Key', 'Value'])
                    writer.writeheader()
                    for key, value in data.items():
                        writer.writerow({'Key': key, 'Value': value})

                else: raise ValueError("Invalid data type for CSV. Supported options: list,dict ")

            print("Data successfully converted from binary to CSV.")
        else:  # file_type == 'binary'
            # Load data from the CSV file
            with open(self.filename, 'r') as csv_file:
                reader = csv.DictReader(csv_file)
                data = [row for row in reader]

            # Save the data to a binary file
            with open(self.filename + '.bin', 'wb') as bin_file:
                pickle.dump(data, bin_file)

            print("Data successfully converted from CSV to binary.")

    def compileConverted(self,data_type):
        return self.compile_dict(data_type)

class CrunchyTxt(Crunchy):
    def __init__(self,filename):
        super().__init__(filename)
    def read_txt(self):
        while True:
            try:
                with open(self.filename,'r') as txt_file:
                    text_data = txt_file.read()
                return text_data
            except FileNotFoundError:
                self.file_exists()


    def find(self,keywords):
        current_position = 0
        text_data = self.read_text().lower()
        keyword_positions = {keyword: [] for keyword in keywords}
        while True:
            for keyword in keywords:
                position = text_data.find(keyword.lower(),current_position)
                if position != -1:
                    keyword_positions[keyword].append(position)
                    current_position = position + 1
                else:
                    current_position = 0
            if all(len(positions) == 0 for positions in keyword_positions.values()):
                break
        return keyword_positions





class CrunchyPanda(Crunchy):
    def __init__(self,filename):
        super().__init__(filename,orientation=None)
    def compile_dict(self,data_type='csv'):
        if data_type== 'df':
            df = pd.read_csv(self.filename)
            return df
        else:
            return super().compile_dict(data_type)

    def filterData(self,filters):
        df = self.compile_dict(data_type='df')
        for column,value in filters.items():
            df = df[df[column]==value]
        return df

    def Cleaner(self, drop_duplicates=True, fillna_value=None,convert_types=None):
        """
               Clean the DataFrame by handling common data cleaning tasks.

               Parameters:
                   drop_duplicates (bool): Whether to drop duplicate rows from the DataFrame (default is True).
                   fillna_value (dict): A dictionary with column names as keys and the value to fill missing
                                        values with as values (default is None).
                   convert_types (dict): A dictionary with column names as keys and the desired data type as values.
                                         For example, {'Age': int, 'Salary': float} (default is None).

               Returns:
                   pandas.DataFrame: The cleaned DataFrame.
               """
        df = self.compile_dict(data_type='df')
        if drop_duplicates:
            df.drop_duplicates(inplace=True)
        if fillna_value:
            df.fillna(fillna_value,inplace=True)
        if convert_types:
            df = df.astype(convert_types)
        return df

    def Reshape(self, pivot_by=None, group_by=None, aggregate_funcs=None):
        """
        Reshape the DataFrame using pivot tables or groupby with aggregations.

        Parameters:
            pivot_by (str or list): Columns to use for pivoting the DataFrame (default is None).
            group_by (str or list): Columns to use for grouping the DataFrame (default is None).
            aggregate_funcs (dict): A dictionary with column names as keys and the aggregation function(s)
                                    to apply as values. For example, {'Salary': 'mean', 'Age': 'max'}.
                                    (default is None).

        Returns:
            pandas.DataFrame: The reshaped DataFrame.
        """
        df = self.compile_dict(data_type='df')

        if pivot_by:
            df_pivot = df.pivot_table(index=pivot_by, values=aggregate_funcs.keys(), aggfunc=aggregate_funcs)
            return df_pivot

        if group_by:
            df_grouped = df.groupby(group_by).agg(aggregate_funcs).reset_index()
            return df_grouped

        return df

import dask as dd

class BigPandaCrunch(CrunchyPanda):
    def __init__(self, filename,speed=16):
        super().__init__(filename)
        self.speed = speed
    def setNparitions(self,speed):
        '''Note: speed = 1 is about 200 mb of RAM
            default speed is 16 or 3.007 gb of RAM
            Set in accordance to computer specifications
             '''
        self.speed = speed

    def compile_dict(self, data_type='csv'):
        if data_type == 'df':
            # Use dask to read the large CSV file as a dask DataFrame
            df = dd.read_csv(self.filename)
            return df
        else:
            return super().compile_dict(data_type)

    def filterData(self, filters):
        df = super().filterData(filters)
        return dd.from_pandas(df, npartitions=self.speed)  # Convert the pandas DataFrame to a dask DataFrame

    def Cleaner(self, drop_duplicates=True, fillna_value=None, convert_types=None):
        df = super().Cleaner(drop_duplicates=drop_duplicates, fillna_value=fillna_value, convert_types=convert_types)
        return dd.from_pandas(df, npartitions=self.speed)  # Convert the pandas DataFrame to a dask DataFrame

    def Reshape(self, pivot_by=None, group_by=None, aggregate_funcs=None):
        df = super().Reshape(pivot_by=pivot_by, group_by=group_by, aggregate_funcs=aggregate_funcs)
        return dd.from_pandas(df, npartitions=self.speed)  # Convert the pandas DataFrame to a dask DataFrame
## With the number of npartitions, it will use 3200 mb of ram by default


'''
# Create an instance of Crunchy and check if the file exists
file_path = 'example.txt'
crunchy = Crunchy(file_path)
if not crunchy.file_exists():
    print(f"The file '{file_path}' does not exist.")
else:
    print(f"The file '{file_path}' exists.")


# Create an instance of CrunchyBin
bin_file_path = 'data.bin'
crunchy_bin = CrunchyBin(bin_file_path)

# Convert the binary data to CSV (list format)
crunchy_bin.Convert(file_type='csv', data_type='list')

# Compile the converted data into a dictionary
converted_data_dict = crunchy_bin.compileConverted(data_type='csv')
print(converted_data_dict)


# Create an instance of CrunchyCSV
csv_file_path = 'data.csv'
orientation_column = 'ID'
crunchy_csv = CrunchyCSV(csv_file_path, orientation_column)

# Determine the orientation column in the CSV file
orientation = crunchy_csv.DetermineOrient()
print(f"The orientation column in '{csv_file_path}' is '{orientation}'.")

# Compile the CSV data into a dictionary
csv_data_dict = crunchy_csv.compile_dict(data_type='csv')
print(csv_data_dict)

Pandas: 
# Create an instance of CrunchyPanda and read the CSV data into a DataFrame
csv_file_path = 'data.csv'
orientation_column = 'ID'
crunchy_panda = CrunchyPanda(csv_file_path, orientation_column)

# Filter the DataFrame to only include rows with Age greater than or equal to 30
filters = {'Age': 30}
filtered_df = crunchy_panda.filter_data(filters)
print(filtered_df)

Reshaping
# Create an instance of CrunchyPanda and read the CSV data into a DataFrame
csv_file_path = 'data.csv'
orientation_column = 'ID'
crunchy_panda = CrunchyPanda(csv_file_path, orientation_column)

# Reshape the DataFrame using pivot tables
pivot_by_columns = ['Category', 'Gender']
aggregate_functions = {'Salary': 'mean', 'Age': 'max'}
pivot_table_df = crunchy_panda.reshape_data(pivot_by=pivot_by_columns, aggregate_funcs=aggregate_functions)
print(pivot_table_df)

# Reshape the DataFrame using groupby with aggregations
group_by_columns = ['Category']
grouped_df = crunchy_panda.reshape_data(group_by=group_by_columns, aggregate_funcs=aggregate_functions)
print(grouped_df)
'''

