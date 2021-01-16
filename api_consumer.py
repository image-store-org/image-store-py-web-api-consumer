import requests

post_payload = {
        
        'title': 'title',
        'orientation': 'PORTRAIT',
        'categories': [
            'NONE',
            'ABSTRACT',
            'ANIMAL'
        ],
        'bytes': [
            81,
            109,
            70,
            122,
            90,
            83,
            65,
            50,
            78,
            67,
            66,
            84,
            100,
            72,
            74,
            108,
            89,
            87,
            48,
            61
        ]}

put_payload = {
        'id': 3,
        'title': 'put_test',
        'orientation': 'PORTRAIT',
        'categories': [
            'NONE',
            'ABSTRACT',
            'ANIMAL'
        ],
        'bytes': [
            81,
            109,
            70,
            122,
            90,
            83,
            65,
            50,
            78,
            67,
            66,
            84,
            100,
            72,
            74,
            108,
            89,
            87,
            48,
            61
        ]}

# TODO separate each entry with \n
def get():
    #print(colored('GET ID({})'.format(id), green))
    print('\x1b[6;30;42m' + 'GET' + '\x1b[0m')
    r = requests.get('https://www.imagestore.vartdalen.com/api/images')
    json_data = r.json()
    print(r)
    print('{}\n'.format(json_data))

def get_id(id):
    print('\x1b[6;30;42m' + 'GET ID({})'.format(id) + '\x1b[0m')
    url = 'https://www.imagestore.vartdalen.com/api/images' + '/{}'.format(id)
    r = requests.get(url)
    json_data = r.json()
    print(r)
    print('{}\n'.format(json_data))

def get_latest():
    print('\x1b[6;30;42m' + 'GET LATEST' + '\x1b[0m')
    url = 'https://www.imagestore.vartdalen.com/api/images/latest'
    r = requests.get(url)
    json_data = r.json()
    print(r)
    print('{}\n'.format(json_data))

def post():
    print('\x1b[6;30;42m' + 'POST' + '\x1b[0m')
    r = requests.post('https://www.imagestore.vartdalen.com/api/images', json = post_payload)
    json_data = r.json()
    print(r)
    print('{}\n'.format(json_data))

# TODO be able to edit payload with keywords e.g: title.TEST
def put(id):
    print('\x1b[6;30;42m' + 'PUT({})'.format(id) + '\x1b[0m')
    url = 'https://www.imagestore.vartdalen.com/api/images' + '/{}'.format(id)
    r = requests.put(url, json = put_payload)
    print('{}\n'.format(r))

def delete(id):
    print('\x1b[6;30;42m' + 'DELETE({})'.format(id)  + '\x1b[0m')
    url = 'https://www.imagestore.vartdalen.com/api/images' + '/{}'.format(id)
    r = requests.delete(url)
    print('{}\n'.format(r))

if __name__ == '__main__':
    get()
    get_id(1)
    post()
    get_latest()
    put(1)