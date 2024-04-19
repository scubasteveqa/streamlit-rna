import pandas as pd
import streamlit as st
import pyodbc

# Connect to Database 
con=pyodbc.connect(driver='postgresql',
           database='pfmegrnargs',
           uid='reader',
           pwd='NWDMCE5xdipIjRrp',
           server='hh-pgsql-public.ebi.ac.uk',
           port=5432)
    

# retrieve a table from the database databases
sql_query = "SELECT * FROM auth_permission"

df = pd.read_sql_query(sql_query, con)

# Display the table
print(df)
