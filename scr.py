import pandas as pd
import numpy as np
import ydata_profiling 
from ydata_profiling import profile_report 
file=pd.read_csv('salaries.csv')
'''
print('************************************')
print(file.describe())
print('************************************')
print(file.info())
print('************************************')
profrep=ydata_profiling.ProfileReport(file)
profrep.to_file('index.html')
'''
dups=file[file.duplicated(keep=False)]
dups.to_csv('dups.csv') 

cleaned=file.drop_duplicates()
cleaned.to_csv('Cleaned.csv')
