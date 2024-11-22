import uuid

import lib
import lib.entity
import lib.service
import lib.storage.json

storage = 'json'

if __name__ == '__main__':
    if storage == 'json':
        storage = lib.storage.json.JSONStorage('./database.json')
    else:
        storage = lib.storage.json.TextStorage('./database.json')

    service = lib.service.Books(storage)

    service.create(lib.entity.Book(
        id=uuid.uuid4(),
        title='Title 1',
        author='Author 1',
        year=2000,
        status=lib.entity.Status.exists
    ))

    service.create(lib.entity.Book(
        id=uuid.uuid4(),
        title='Title 2',
        author='Author 2',
        year=2000,
        status=lib.entity.Status.exists
    ))

    service.delete('40841259-799d-4910-b4c6-6c53d58a8629')

    service.search('author', 'Author 1')
