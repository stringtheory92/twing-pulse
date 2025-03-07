import streamlit as st
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col


# Initialize Snowflake session
def create_session():
    connection_parameters = {
        "account": "<your_account>",
        "user": "<your_user>",
        "password": "<your_password>",
        "role": "<your_role>",
        "warehouse": "<your_warehouse>",
        "database": "<your_database>",
        "schema": "<your_schema>",
    }
    return Session.builder.configs(connection_parameters).create()


session = create_session()


# Query data from a Snowflake table
def load_data():
    df = session.table("your_table_name").select(col("column1"), col("column2"))
    return df.to_pandas()


# Streamlit app layout
st.title("Snowflake Native App with Streamlit")
st.write("Fetching data from Snowflake...")
data = load_data()
st.dataframe(data)
