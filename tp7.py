# coding: utf-8

from lxml import etree


class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)


class Book:
    def __init__(self, id, title, author, genre, price, publish_date, description):
        self.id = id
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price
        self.publish_date = publish_date
        self.description = description

xml_doc = etree.parse('file.xml')
root = xml_doc.getroot()

authors = {}
xml_books = root.findall('book')
for xml_book in xml_books:
    book = Book(
        xml_book.attrib['id'],
        xml_book.find('title').text,
        xml_book.find('author').text,
        xml_book.find('genre').text,
        xml_book.find('price').text,
        xml_book.find('publish_date').text,
        xml_book.find('description').text
    )

    author_name = xml_book.find('author').text
    author = Author(author_name)
    if not author_name in authors:
        authors[author_name] = author

    authors[author_name].add_book(book)


# Affichage du résultat
for author in authors.values():
    print('Auteur : {}'.format(author.name))
    print('  Ouvrages :')
    for ouvrage in author.books:
        print('    {}'.format(ouvrage.title))
