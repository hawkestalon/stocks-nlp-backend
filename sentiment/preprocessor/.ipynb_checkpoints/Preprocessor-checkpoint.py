import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob



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

def apply_spacy_pipe(text_list):
    '''
    @param text_list: since nlp.pipe() works best with large amounts of data,
    it is best to use list of large amounts of text.
    @return returns a Doc object from spacy pipeline
    '''
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe('spacytextblob')
    return nlp.pipe(text_list)
