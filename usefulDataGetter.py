import json
from requestApi import requestApi

class usefulDataGetter:
    def __init__(self, title:str = None, author:str = None) -> None:
        self.books_response = requestApi(title,author).fetchBooks()

    def data2json(self) -> dict:
        json_response = json.loads(self.books_response)
        return json_response

    def extractInfo(self, raw_docs:dict):
        raw_docs
        pass

    def main(self):
        raw_dictionary = self.data2json()
        raw_docs = raw_dictionary.get('docs')

        pass


