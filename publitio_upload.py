from constants import *
from publitio import PublitioAPI

publitio_api = PublitioAPI(key=PUBLITIO_API_KEY, secret=PUBLITIO_API_SECRET)

def upload_to_publitio(file):
    with open(file, 'rb') as f:
        result = publitio_api.create_file(file=f, title='test title', description='test description')
    return result


def delete_from_publitio(file):
    # TODO
    pass