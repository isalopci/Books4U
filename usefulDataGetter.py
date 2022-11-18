from requestApi import requestApi

class usefulDataGetter:
    def __init__(self, title:str = None, author:str = None) -> None:
        self.books_response = requestApi(title,author).fetchBooks()

    @staticmethod
    def extractTitle(raw_doc:dict):
        return raw_doc.get('title')

    @staticmethod
    def extractAuthors(raw_doc:dict):
        authors = raw_doc.get('author_name')
        return ', '.join(authors)

    def fetchRawDocs(self):
        raw_dictionary = self.books_response
        return raw_dictionary.get('docs')
