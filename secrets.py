import pandas as pd
import streamlit as st
import pyodbc
import os

# Retrieve environment variables directly
driver = os.environ.get('DB_DRIVER')
database = os.environ.get('DB_DATABASE')
uid = os.environ.get('DB_UID')
pwd = os.environ.get('DB_PWD')
server = os.environ.get('DB_SERVER')
port = os.environ.get('DB_PORT')

# Create the connection string for pyodbc
connection_string = f'DRIVER={{{driver}}};DATABASE={database};UID={uid};PWD={pwd};SERVER={server};PORT={port}'

# Connect to Database 
con = pyodbc.connect(connection_string)

# Retrieve a table from the database
query = "SELECT * FROM auth_permission"

# Execute query and read into DataFrame
df = pd.read_sql(query, con)

# Display the table in Streamlit
st.dataframe(df)
