import pandas as pd 
def merge_data(meta, author, lang): 
    '''Function to merge the metadata, author and language dataframes'''
    meta_author = pd.merge(meta, author, on=["gutenberg_author_id", "author"])
    data = pd.merge(meta_author, lang,  on=["gutenberg_id", "language"])
    return(data)