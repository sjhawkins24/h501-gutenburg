import pandas as pd 
def grouping_fun(data): 
    '''Function that will group the data by alias and then sort'''
    data = data.groupby("alias")\
        ["language"].count().\
            to_frame().\
                sort_values(by = "language", ascending = False)
    return_list = data.index.to_list()
    return(return_list)