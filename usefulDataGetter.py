from requestApi import requestApi

class usefulDataGetter:
    def __init__(self, title:str = None, author:str = None) -> None:
        self.books_response = requestApi(title,author).fetchBooks()

    def fetchRawDocs(self):
        raw_dictionary = self.books_response
        return raw_dictionary.get('docs')
