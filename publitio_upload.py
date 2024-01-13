from constants import *
from publitio import PublitioAPI

publitio_api = PublitioAPI(key=PUBLITIO_API_KEY, secret=PUBLITIO_API_SECRET)

with open('/Users/samuelxing/instagram_bot/red_panda_test.jpeg', 'rb') as f:
    result = publitio_api.create_file(file=f, title='test title', description='test description')

print(result)