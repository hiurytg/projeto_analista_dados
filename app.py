import requests
import pandas as pd
import streamlit as st
import pandasql as psql
import sqlite3 as sqlite

source = "C:\\Users\\Hiurytg.000\\Desktop\\projeto_ipm_analista_dados\\licitacoes.csv"
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

