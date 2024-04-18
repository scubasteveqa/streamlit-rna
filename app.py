import pandas as pd
import psycopg2
import psycopg2.extras
import sqlalchemy
import streamlit as st
import pydoc    


def get_connection():
    # Connect to Database
    #engine = sqlalchemy.create_engine(
    #    "postgresql+psycopg2://reader:NWDMCE5xdipIjRrp@hh-pgsql-public.ebi.ac.uk/pfmegrnargs")

    
con=pyodbc.connect(driver='{postgresql}',
                   database='pfmegrnargs',
                   uid='reader',
                   pwd='NWDMCE5xdipIjRrp',
                   server='hh-pgsql-public.ebi.ac.uk',
                   port=5432)
    
    #PWD = Sys.getenv("CONNECTION_RNA_CENTRAL_PASSWORD"), BoolsAsChar = "NWDMCE5xdipIjRrp", 
    #timeout = 10)

    # retrieve a table from the database databases
    query = "SELECT * FROM auth_permission"

    df = pd.read_sql_query(query, engine)

    # Display the table
    df


if __name__ == "__main__":
    get_connection()
