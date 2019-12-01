#Functions used in Data Wrangling Jupyter Notebook
import pandas as pd

#remove any leading or trailing whitespace in a specific column of a dataframe
def strip_column(df, column):
    df[column] = df[column].str.strip()

#change names of a cell in one dataframe to match name of cell in another dataframe
def change_name(df, rowIndex, columnIndex, name):
    df.loc[rowIndex, columnIndex] = name

#merge two dataframes
def merge_df(df1, df2, on, how):
    newDF = df1.merge(df2, on=on, how=how)
    return newDF

#slice country column from Dataframe
def get_countries(df):
    countries = df[['Country']]
    return countries

#return differences between two dataframes
def diff_df(df1, df2, key1, key2, keep):
    diff = pd.concat([df1, df2], keys=[key1, key2]).drop_duplicates(keep=keep)
    return diff

#remove row in dataframe based on hierarchical multiindex
def remove_country(masterdf, index1, dropdf):
    df_remove = masterdf.loc[index1, :].index
    clean_df = dropdf.drop(df_remove, axis=0)
    return clean_df