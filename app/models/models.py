class Publisher:
    def __init__(self, publisher_id, name, address_line1, address_line2, city, country, email):
        self.publisher_id = publisher_id
        self.name = name
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.city = city
        self.country = country
        self.email = email


class Author:
    def __init__(self, first_name, last_name, email, country):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.country = country


class Book:
    def __init__(self, book_id, title, pages, price, edition, publisher, authors):
        self.book_id = book_id
        self.title = title
        self.pages = pages
        self.price = price
        self.edition = edition
        self.publisher = publisher
        self.authors = authors

