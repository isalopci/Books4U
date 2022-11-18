import streamlit as st
from usefulDataGetter import usefulDataGetter as fetch

st.title('BOOKS :)')
st.caption("A work done by Isabella López")

search1, search2, search3, search4 = st.columns(4)
#Column1
selection = search1.selectbox(label = 'Select your search type', options = ['Author', 'Title'])
#Column2
author = None
title = None
if selection == 'Author':
    author = search2.text_input(label = "Insert the authors name")
if selection == 'Title':
    title = search2.text_input(label = "Insert the title of a book")
#Column3
limit = search3.number_input(label = 'Insert the max number of results', min_value=1, max_value=100, value=10, label_visibility="visible")
#Column4
size = search4.selectbox(label = 'Size of books cover', options=['S', 'M', 'L'])
