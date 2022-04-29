from employees.employees import employees
from sales.sales import sales
import streamlit as st

def run():
    st.title("Welcome in your imaginary compyny")
    num_emp = st.slider("Enter how many employees in your Company")
    table1 = employees(num_emp)
    st.write(table1.emp_table())
    num_sales = st.slider("Enter how many sales in your Company")
    table2 = sales(num_sales)
    st.write(table2.sales_table())

if __name__ == "__main__":
    run()
