import streamlit as st
import pandas as pd
from io import StringIO

st.title("Zerodha Tradebook visualizer")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.caption("File uploaded succesfully!")
    dataframe = pd.read_csv(uploaded_file)

    subset_df = dataframe[["trade_date", "quantity", "price","trade_type"]]
    unique_dates = subset_df["trade_date"].unique()
    unique_trade_types = subset_df["trade_type"].unique()
    st.write(unique_trade_types)
    iterated_dict = {}
    iterated_dict_2 = {}

    # for index, row in subset_df.iterrows():
    #     if row['trade_type'] == 'buy':
    #         if row['trade_date'] in iterated_dict:
    #             iterated_dict[row['trade_date']] = iterated_dict[row['trade_date']] + row['price'] * row['quantity']
    #         else:
    #             iterated_dict[row['trade_date']] = row['price'] * row['quantity']
    #     # st.write(row['trade_date'], row['quantity'], row["price"], row['quantity'] * row["price"])
    # for index, row in subset_df.iterrows():
    #     if row['trade_type'] == 'sell':
    #         if row['trade_date'] in iterated_dict_2:
    #             iterated_dict_2[row['trade_date']] = iterated_dict_2[row['trade_date']] + row['price'] * row['quantity']
    #         else:
    #             iterated_dict_2[row['trade_date']] = row['price'] * row['quantity']

    st.write(unique_dates)
    
    st.write(iterated_dict)
    st.write(iterated_dict_2)
    st.table(data=iterated_dict)

