import streamlit as st
import json

# Load data
with open('scrapy_project/data/books.json') as f:
    books = json.load(f)

st.title('Books to Scrape')
st.write('List of Books:')
  
for book in books:
    st.subheader(book['title'])
    st.write(f"Price: {book['price']}")
    st.write(f"Availability: {book['availability']}")
