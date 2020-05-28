def count_missing_value(df):
  '''
  Counting missing values for each column.

  Parameters:
    df (DataFrame): The pandas DataFrame.

  '''

  for column in df.columns:
    print("number of NaN values for the column " + str(column) + 
          " :", df[column].isnull().sum())

def replace_missing_value_with_mean(df, column_name):
  '''
  Replacing the missing values of the column 'column_name' with the 
  mean of the column 'column_name'  using the method replace()

  Requirement: 
    import numpy as np

  Parameters:
    df (DataFrame): The pandas DataFrame.
    column_name (str): A column's name.

  '''

  mean=df[column_name].mean()
  df[column_name].replace(np.nan,mean, inplace=True)


def count_rows_category(df, cate_column_name):
  '''
  Count the number of rows with unique column values and return a dataframe

  Parameters:
    df (DataFrame): The pandas DataFrame.
    cate_column_name (str): A categorical column's name.
  '''

  df_val_count = df[cate_column_name].value_counts().to_frame().reset_index()
  df_val_count.columns = [cate_column_name, 'count']
  return df_val_count

def convert_column_headers_2str(df):
  '''
  Convert the type of column headers to string

  Parameters:
    df (DataFrame): The pandas DataFrame.
  '''

  df.columns = list(map(str, df.columns))
  [print (x + ': ', type(x)) for x in df.columns.values]
