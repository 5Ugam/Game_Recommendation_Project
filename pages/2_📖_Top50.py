import streamlit as st
import pandas as pd
st.title("Top 50 games by User Rating")

top50 = pd.read_csv(r"data_files\top50.csv", index_col="Unnamed: 0")
top50.rename(columns={"name": "Name",
"num_rating":"Total no of Rating",
"avg_rating":"Average Rating",
"boardgamepublisher":"Publisher",
"boardgamecategory":"Category"},inplace = True)
st.dataframe(data=top50, height=600)
