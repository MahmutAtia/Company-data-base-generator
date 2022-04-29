import random
from random import randint
import pandas as pd
from employees.employees import employees
from sales.constants import *


class sales:
    df2 = pd.DataFrame({"ID": [], "number of sales": [], "price": [], "profit": [], "COG": [],
                        "product": []})  # second table "sales"
    def __init__(self,num_of_sales):
        self.num_of_sales = num_of_sales

    def sales_table(self):
        for n in range(
                int(self.num_of_sales)):  # sales table #range(num_of_employees) gives error but without range there is a problems with the number of loops
            id = random.choice(employees.df.ID)  # get a random num from a list
            numberofsales = randint(1, 30)
            price = randint(20000, 50000)
            profit = randint(2000, 5000)
            cog = price - profit
            product = random.choice(letters)
            sales.df2.loc[len(sales.df2.index)] = [id, numberofsales, price, profit, cog, product]
        return sales.df2


