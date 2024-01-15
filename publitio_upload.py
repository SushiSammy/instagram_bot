from constants import *
from publitio import PublitioAPI

publitio_api = PublitioAPI(key=PUBLITIO_API_KEY, secret=PUBLITIO_API_SECRET)

def upload_to_publitio(file):
    print('Beginning upload to Publitio...')
    with open(file, 'rb') as f:
        result = publitio_api.create_file(file=f, title='test title', description='test description')
    print('Finished upload to Publitio...')
    return result


def delete_from_publitio(id):
    print('Deleting file from Publitio...')
    publitio_api.delete_file(id)
    print('Done deleting file from Publitio...')