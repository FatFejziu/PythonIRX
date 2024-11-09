import pandas as pd
import streamlit as st
import plotly.express as px
from numpy.ma.extras import unique
from streamlit import columns

# st.header("Welcome to Lesson 18")
# df=pd.DataFrame({
#     "Name":["Alma","Blini","Klea"],
#     "Age":[27,17,17],
#     "City":["Ferizaj","Podujev","Podujev"]
# })
# st.dataframe(df)

books_df=pd.read_csv("bestsellers_with_categories_2022_03_27.cvs")
st.title("Bestselling books Analysis")
st.write("This app analyses the amazon top selling books from 2009 to 2022")

st.subheader("Summary statics")
total_books=books_df.shape[0]
unique_title=books_df["Name"].nunique()
ave_rating=books_df["User Rating"].mean()
ave_price=books_df["Price"].mean()

col1,col2,col3,col4=st.columns(4)
col1.metric("Total Books",total_books)
col2.metric("Unique Titles",unique_title)
col3.metric("Averrage Titles",ave_rating)
col4.metric("Averrage price",ave_price)


st.header("Dataset Priview")
st.write(books_df.head())


col1,col2=columns(2)

with col1:
    st.subheader("Top 10 book title")
    top_titles=books_df["Name"].value_counts().head(10)
    st.bar_chart(top_titles)
with col2:
    st.subheader("Top 10 Authors")
    top_authors=books_df["Author"].value_counts().head(10)
    st.bar_chart(top_authors)

st.subheader("Genre Distibution")
fig=px.pie(books_df, names="Genre",title="Most liked Genre (2009-2022)", color="Genre",color_discrete_secuence=px.colors.sequential.Plasma)
st.plotly_chart(fig)