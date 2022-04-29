import re
from random import randint
import names
import pandas as pd
from employees.constants import *


class employees:
    df = pd.DataFrame({"ID": [], "First Name": [], "Last Name": [], "Gender": []})  # frist table "employee"
    def __init__(self,num_of_employees):
        self.num_of_employees=num_of_employees

    def emp_table(self):
        for i in range(int(self.num_of_employees)):
            ID = randint(1234567, 2345678)
            frist_name = names.get_first_name()
            if re.findall(frist_name,male, re.I): #i couldn't write it as r"first"
                Gender = "male"
            else:
                 Gender = "female"

            last_name = names.get_last_name()
            employees.df.loc[len(employees.df.index)] = [ID, frist_name, last_name, Gender] #insert a row inside the dataframe
        return employees.df

