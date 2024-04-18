import pandas as pd
import psycopg2
import psycopg2.extras
import sqlalchemy
import streamlit as st


def get_connection():
    # Connect to Database
    #engine = sqlalchemy.create_engine(
    #    "postgresql+psycopg2://reader:NWDMCE5xdipIjRrp@hh-pgsql-public.ebi.ac.uk/pfmegrnargs")

    con <- dbConnect(odbc::odbc(), Driver = "postgresql", Server = "hh-pgsql-public.ebi.ac.uk", 
    Port = "5432", Database = "pfmegrnargs", UID = "reader", PWD = "NWDMCE5xdipIjRrp", timeout = 10
    
    #PWD = Sys.getenv("CONNECTION_RNA_CENTRAL_PASSWORD"), BoolsAsChar = "NWDMCE5xdipIjRrp", 
    #timeout = 10)

    # retrieve a table from the database databases
    query = "SELECT * FROM auth_permission"

    df = pd.read_sql_query(query, engine)

    # Display the table
    df


if __name__ == "__main__":
    get_connection()
