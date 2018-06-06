

import os
import pandas as pd

def get_filenames(path):
    filenames = []
    for i in os.walk(path):
        for filename in i[-1]:
            full_filename = os.path.join(i[0],filename)
            filenames.append(full_filename)
            
    return filenames
    

def read_excel(filename):
    df = pd.read_excel(filename, index_col=None, headers=0, na_values=['NA'])
    return df
    
def merge_excel(datas):
    
    return pd.concat(datas, ignore_index=False)
    

if __name__ == '__main__':
    print 'Program is running.....'
    path = r'C:\Users\John\Desktop\VCS\EDD'
    target_path =r'C:\Users\John\Desktop\VCS\EDD'
    data = []
    for filename in get_filenames(path):
        data.append(read_excel(filename))
    
    df = merge_excel(data)
    df.to_excel(target_path+os.sep+'All.xlsx', index=False)
    print 'Success!' 
    