from requestApi import requestApi

class usefulDataGetter:
    def __init__(self, title:str = None, author:str = None) -> None:
        self.books_response = requestApi(title,author).fetchBooks()

    @staticmethod
    def extractTitle(raw_doc:dict) -> str:
        return raw_doc.get('title')

    @staticmethod
    def extractAuthors(raw_doc:dict) -> str:
        authors = raw_doc.get('author_name')
        return ', '.join(authors)

    @staticmethod
    def extractPublicationYear(raw_doc:dict) -> str:
        return raw_doc.get('first_publish_year')

    def fetchRawDocs(self) -> list[dict]:
        raw_dictionary = self.books_response
        return raw_dictionary.get('docs')
