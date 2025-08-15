#IMPORTS GO HERE
import numpy as np
import pandas as pd
from matplotlib import pyplot


#CSV READING DEFINITIONS GO HERE
print("-----------------------------------------------")
file_name = input("Welcome to the infastructrue CLI: Enter a database you want to read: " )
print("-----------------------------------------------")

df=pd.read_csv(file_name)
df_incomplete = df[df['status'].str.lower() != 'Complete']
complete_projects = df['status'].str.lower().str.startswith('complete', na=False).sum()

# print("this is whats going on",df_incomplete)
# df_incomplete.to_csv('incomplete_projects.csv', index=False)


#CALCULATIONS GO HERE
total=len(df)
incomplete_projects = total - complete_projects
Percent_complete = (complete_projects/ total) *100
Percent_incomplete = (incomplete_projects/ total) *100

#DISPLAYS GO HERE
print("-----------------------------------------------")
print("CSV Data information: ")
print("-----------------------------------------------")

print ("Total Lines: ", total)
print("Percentage of projects Completed: {:.2f}%".format(Percent_complete))
print("Percentage of projects Incompleted: {:.2f}%".format(Percent_incomplete))

print("-----------------------------------------------")