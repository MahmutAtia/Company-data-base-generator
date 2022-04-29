import random
import re
from random import seed
from random import randint
import names
import openpyxl as openpyxl
import pandas as pd
import os
import string











#save file
try:
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') # finding desktop path windows
except:
    desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') # or finding it in mac

path = desktop+"\excel generator" #path to creating the direktory

try:  # creating the directory and saving the excel file
     os.mkdir(path)
     with pd.ExcelWriter(path + '\generated_employments_table.xlsx') as writer:
         df.to_excel(writer, sheet_name= "employees", index= False)
         df2.to_excel(writer, sheet_name= "sales", index= False)

#     df.to_excel(path + '\generated_employments_table.xlsx')

# with pd.writer(path + "\generated_employments_table.xlsx") as writer:
    #    df.to_excel(writer)
   # df.to_excel(path + '\generated_employments_table.xlsx', index= False)

except : #if the directory already exist
    with pd.ExcelWriter(path + '\generated_employments_table.xlsx', mode= "w") as writer: # you get error when you forget mode =
        df.to_excel(writer, sheet_name="employees", index=False)
        df2.to_excel(writer, sheet_name="sales", index=False)
        #writer.close() # solving opend file problem
print("thanks for wating you already have your data")