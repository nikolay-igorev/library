import unittest.mock

import lib.entity
import lib.repository


def test_add_book():
    book = lib.entity.Book(
        id="id",
        title="title",
        author="author",
        year=2000,
        status=lib.entity.Status.exists,
    )

    storage = unittest.mock.Mock(spec=lib.repository.Storage)
    storage.list.return_value = []

    repository = lib.repository.Books(storage)
    repository.create(book)

    storage.put.assert_called_with([book])


def test_delete_book():
    book = lib.entity.Book(
        id="id",
        title="title",
        author="author",
        year=2000,
        status=lib.entity.Status.exists,
    )

    storage = unittest.mock.Mock(spec=lib.repository.Storage)
    storage.list.return_value = [book]

    repository = lib.repository.Books(storage)
    repository.delete(book.id)

    storage.put.assert_called_with([])


def test_change_status_book():
    book = lib.entity.Book(
        id="id",
        title="title",
        author="author",
        year=2000,
        status=lib.entity.Status.exists,
    )

    storage = unittest.mock.Mock(spec=lib.repository.Storage)
    storage.list.return_value = [book]

    repository = lib.repository.Books(storage)

    repository.change_status(book.id, lib.entity.Status.reserved)
    book.status = lib.entity.Status.reserved

    storage.put.assert_called_with([book])


def test_search_books():
    books_author1 = [
        lib.entity.Book(
            id="1",
            title="title1",
            author="author1",
            year=2000,
            status=lib.entity.Status.exists,
        ),
        lib.entity.Book(
            id="2",
            title="title2",
            author="author1",
            year=2000,
            status=lib.entity.Status.exists,
        ),
    ]

    books = books_author1 + [lib.entity.Book(
        id="3",
        title="title3",
        author="author2",
        year=2001,
        status=lib.entity.Status.exists,
    )]

    storage = unittest.mock.Mock(spec=lib.repository.Storage)
    storage.list.return_value = books

    repository = lib.repository.Books(storage)

    assert repository.search("author", "author1") == books_author1
