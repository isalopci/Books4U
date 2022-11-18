import streamlit as st
from usefulDataGetter import usefulDataGetter as fetch

# Script to create the interface with streamlit and show the books search results in it

def createInterface() -> None:

    st.title('BOOKS 4 U :)')
    st.caption("By Isabella López Cifuentes")

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
    limit = search3.number_input(label = 'Insert number of results', min_value=1, max_value=100, value=10, label_visibility="visible")
    
    #Column4
    size = search4.selectbox(label = 'Size of books cover', options=['S', 'M', 'L'])
    return title,author,limit,size


def displayBooksSearch(title, author,limit, size) -> None:
    if title or author:

        list_docs = fetch(title, author).fetchRawDocs()
        len_list = len(list_docs)

        for doc in list_docs[:limit]:

            st.image(image = fetch.extractImage(doc, size))
            with st.container():
                st.write(f'Title: {fetch.extractTitle(doc)}')
                st.write(f'Authors: {fetch.extractAuthors(doc)}')
                st.write(f'Publication date: {fetch.extractPublicationYear(doc)}')
                st.write(f'Average book length: {fetch.extractBookPages(doc)}')

# Driver Code
if __name__ == '__main__':
    title, author, limit, size = createInterface()
    displayBooksSearch(title, author,limit, size)
            