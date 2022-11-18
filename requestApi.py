import requests

class requestApi:
    def __init__(self, title:str = None, author:str = None) -> None:
        self.title = title 
        self.author = author 
        
    def buildUrl(self) -> str:

        base_url = 'http://openlibrary.org/search.json'

        if self.author:
            query = f'?author={self.author}'
        elif self.title:
            query = f'?title={self.title}'
        
        return base_url + query

    def fetchBooks(self):
        url = self.buildUrl()
        response = requests.get(url)
        return response.text
#if __name__ == '__main__':
#    requestApi().fetchBooks()