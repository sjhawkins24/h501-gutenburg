import pandas as pd 
def merge_data(meta, author, lang): 
    meta_author = pd.merge(meta, authors, on=["gutenberg_author_id", "author"])
    data = pd.merge(meta_author, lang,  on=["gutenberg_id", "language"])
    return(data)