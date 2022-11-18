from requestApi import requestApi
# This class obtains the useful information of a doc dictionary that throws the API response. Here it ensures to show only the important information
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

    @staticmethod
    def extractBookPages(raw_doc:dict) -> str:
        return raw_doc.get('number_of_pages_median')

    # Extract image with default size L when not given
    @staticmethod
    def extractImage(raw_doc:dict, size:str = 'L') -> str:
        cover_image_id = raw_doc.get('cover_i')
        return requestApi.fetchCoverImage(cover_image_id, size)

    def fetchRawDocs(self) -> list[dict]:
        raw_dictionary = self.books_response
        return raw_dictionary.get('docs')
