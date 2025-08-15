
import numpy as np
import pandas as pd
from matplotlib import pyplot

df=pd.read_csv('Ontario_infaprojects_clean.csv')


df_incomplete = df[df['status'].str.lower() != 'Complete']
complete_projects = df['status'].str.lower().str.startswith('complete', na=False).sum()

# print("this is whats going on",df_incomplete)

# df_incomplete.to_csv('incomplete_projects.csv', index=False)
total=len(df)
print ("this is total", total)
incomplete_projects = total - complete_projects
Percent_complete = (complete_projects/ total) *100
Percent_incomplete = (incomplete_projects/ total) *100
print(Percent_complete)
print(Percent_incomplete)