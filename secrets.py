import pandas as pd
import streamlit as st
import pyodbc
import os
from dotenv import load_dotenv

# Load environment variables from .env file (if using .env)
load_dotenv()

# Retrieve environment variables
driver = os.getenv('DB_DRIVER')
database = os.getenv('DB_DATABASE')
uid = os.getenv('DB_UID')
pwd = os.getenv('DB_PWD')
server = os.getenv('DB_SERVER')
port = os.getenv('DB_PORT')

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
