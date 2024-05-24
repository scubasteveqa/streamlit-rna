import pandas as pd
import streamlit as st
import pyodbc
import os

# Retrieve environment variables
driver = os.environ('DB_DRIVER')
database = os.environ('DB_DATABASE')
uid = os.environ('DB_UID')
pwd = os.environ('DB_PWD')
server = os.environ('DB_SERVER')
port = os.environ('DB_PORT')

# Connect to Database 
con=pyodbc.connect(
    driver=driver,
    database=database,
    uid=uid,
    pwd=pwd,
    server=server,
    port=port
)
    

# retrieve a table from the database databases
query = "SELECT * FROM auth_permission"

df = pd.read_sql_query(query, engine)

# Display the table
df
