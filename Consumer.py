import requests, os
from api_token import get_token

class Consumer:
    def __init__(self):
        self.headers = {'Authorization': 'Bearer ' + get_token()}
        self.post_payload = {'title': 'post_test', 'orientation': 'PORTRAIT', 'categories': 
                                ['NONE', 'ABSTRACT', 'ANIMAL'], 'bytes': [81,109,
                                    70, 122, 90, 83, 65, 50, 78, 67, 66, 84, 100,
                                    72, 74, 108, 89, 87, 48, 61]}
        self.put_payload = {'title': 'put_test', 'orientation': 'PORTRAIT', 'categories': 
                                ['NONE', 'ABSTRACT', 'ANIMAL'], 'bytes': [81,109,
                                    70, 122, 90, 83, 65, 50, 78, 67, 66, 84, 100,
                                    72, 74, 108, 89, 87, 48, 61]}
    
    # helper function for url
    def url(self, path = ''):
        return 'https://www.imagestore.vartdalen.com/api/images/' + str(path)
    
    # TODO separate each entry with \n
    # get all data entries
    def get(self):
        return requests.get(self.url(), headers = self.headers)

    # get a data entry by id
    def get_id(self, id):
        return requests.get(self.url(id), headers = self.headers)

    # get latest data entry
    def get_latest(self):
        return requests.get(self.url('latest'), headers = self.headers)

    # post a data entry, id incremented by internal mySQL counter
    def post(self):
        return requests.post(self.url(), json = self.post_payload, headers = self.headers)

    # TODO be able to edit payload with keywords e.g: title.TEST
    # edit existing data entry by id
    def put(self, id):
        return requests.put(self.url(id), json = self.put_payload, headers = self.headers)

    # delete data entry by id
    def delete(self, id):
        return requests.delete(self.url(id), headers = self.headers)

