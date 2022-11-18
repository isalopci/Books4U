BOOKS 4 U 

Author: Isabella Lopez Cifuentes

Description: 

This simple application lets you search books by author name or by title showing the most important imformation. This information includes the book cover, title, author, book length in pages and publication date. 


For this I used Search and Covers APIs from Open Library (https://openlibrary.org/developers/api) to get the information about the books. 

Usage:

This application was programmed using Python 3.9.2, therefore in order to run the application, it is necessary to have at least this version of python. 

Fulfilling the python requirement, you only need to install some dependencies. Open your terminal, cd into the directory test1. Once there, install the dependencies by running (using PyPI):

pip install -r requirements.txt

Once the streamlit and requests libraries are installed, you can start the application by running:

python -m streamlit run web.py

wait for your default internet browser to load the streamlit interface and start searching your books :D

1. You must select the type of search: by author or by title. 
2. Then you must give the authors name or title of teh book
3. Give the number of results you want the application to show you
4. Give the the size or how big you want the book cover images to be shown. 
