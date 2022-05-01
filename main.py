from employees.employees import employees
from sales.sales import sales
import streamlit as st

def run():

    st.title("Welcome in your imaginary company")
    st.markdown("#### generate an imaginary company data to help you in learning SQL, Tableau Excel pandas,etc ")
    st.image("https://jeffbittner.com/wp-content/uploads/local-marketing-consultant-nj-1.jpg")
    num_emp = st.sidebar.slider("Enter how many employees in your Company")
    table1 = employees(num_emp)
    st.write(table1.emp_table())
    st.download_button("Download your employee table", data = table1.csv())
    num_sales = st.sidebar.slider("Enter how many sales in your Company")
    table2 = sales(num_sales)
    st.write(table2.sales_table())
    st.download_button("Download your sales table", data = table2.csv())


if __name__ == "__main__":
    run()
