import pandas as pd
import streamlit as st
import pyodbc
import os

# Retrieve environment variables
driver = os.getenv('DB_DRIVER')
database = os.getenv('DB_DATABASE')
uid = os.getenv('DB_UID')
pwd = os.getenv('DB_PWD')
server = os.getenv('DB_SERVER')
port = os.getenv('DB_PORT')

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
