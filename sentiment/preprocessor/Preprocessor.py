import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import re



def remove_duplicates(df, column_name):
    '''
     @param df: dataframe with the text
     @param column_name: name of the column that you want to use as basis
     @return returns a df without duplicates that have been removed based on the basis
    '''
    return df.drop_duplicates(column_name)


def create_text_list(df, column_name):
    '''
    @param df: takes a dataframe and turns the given column into a list
    @param column_name: column that will be turned into a list
    @return returns a list from a dataframe column
    '''
    return df[column_name].tolist()


def filter_by_ticker(text_list, stock_ticker):
    '''
    @param text_list: list of text content
    @param stock_ticker: symbol representing the stock on the market
    @return: a list of text content IFF it contains stock_ticker
    '''
    filtered_list = []
    for text in text_list:
        if re.search(rf'\s{stock_ticker}\s', text) or re.search(rf'\s\${stock_ticker}\s', text):
            filtered_list.append(text)
    return filtered_list


