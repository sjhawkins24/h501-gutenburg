from tt_gutenberg import mod1, mod2
import pandas as pd
def list_authors(by_languages=True, alias=True):
    '''Big function that will produce the final output asked for'''
    #Start by reading in the data 
    authors = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv")
    lang = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv")
    meta = pd.read_csv("https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv") 
    #Use the function in the first module to merge the data sets
    data = mod1.merge_data(meta, authors, lang)
    #Then use the function in the second module to do the grouping and sorting
    return_list = mod2.grouping_fun(data)
    return(return_list)   