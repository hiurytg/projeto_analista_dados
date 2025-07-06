import pandas as pd
import streamlit as st
import sqlite3 as sqlite
import toml
import bcrypt

# Load secrets
db_password = st.secrets.db_credentials.password

# Function to check password
def check_password(password):
    if db_password == password:
        return True
    return False

# Login form
def login():
    st.title("Login")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if check_password(password):
            st.session_state["logged_in"] = True
            st.success("Logged in successfully!")
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

# Main app logic
if "logged_in" not in st.session_state:
    login()
else:    
    source = "licitacoes.csv"
    conn   = sqlite.connect('licitacoes.db')
    df     = pd.read_csv(source, delimiter =';', on_bad_lines = 'skip')
    query  = "SELECT * FROM tblicitacoes limit 20" 
    
    df.to_sql('tblicitacoes', conn, if_exists='replace') 
    
    result_df = pd.read_sql_query(query, conn)
    
    
    # Streamlit
    st.title("Dados de licitações no Brasil")
    st.write("Tabela oficial .gov:")
    st.dataframe(result_df)
    
    # Add more interactive elements as needed
    if st.button('Show Summary'):
        st.write(result_df.describe())
    
    conn.close()
    
