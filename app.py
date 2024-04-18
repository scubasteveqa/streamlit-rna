import pandas as pd
import streamlit as st
import pyodbc

#def get_connection():
# Connect to Database 
con=pyodbc.connect(driver='postgresql',
           database='pfmegrnargs',
           uid='reader',
           pwd='NWDMCE5xdipIjRrp',
           server='hh-pgsql-public.ebi.ac.uk',
           port=5432)
    

# retrieve a table from the database databases
query = "SELECT * FROM auth_permission"

df = pd.read_sql_query(query, engine)

# Display the table
df


if __name__ == "__main__":
    get_connection()
