from app.domain.models import Book

class BookRepository:
    def __init__(self, db):
        self.db = db

    def save(self, book_dto):
        new_book = Book(**book_dto.__dict__)
        self.db.session.add(new_book)
        self.db.session.commit()
        return new_book

    def get_all(self):
        return self.db.session.query(Book).all()

    def get_by_id(self, book_id):
        return self.db.session.query(Book).filter_by(book_id=book_id).first()

    def update(self, book_id, updated_book):
        book = self.get_by_id(book_id)
        if book:
            for key, value in updated_book.items():
                setattr(book, key, value)
            self.db.session.commit()
        return book

    def delete(self, book_id):
        book = self.get_by_id(book_id)
        if book:
            self.db.session.delete(book)
            self.db.session.commit()
        return book

