class BookService:
    def __init__(self, book_repository):
        self.book_repository = book_repository

    def create_book(self, book_dto):
        book = self.book_repository.save(book_dto)
        return book

    def get_all_books(self):
        books = self.book_repository.get_all()
        # Convert domain models to DTOs
        return [BookDTO(
            title=book.title,
            pages=book.pages,
            price=book.price,
            edition=book.edition,
            publisher=book.publisher,  # Assume PublisherDTO exists
            authors=book.authors  # Assume list of AuthorDTO
        ) for book in books]

    def get_book_by_id(self, book_id):
        return self.book_repository.get_by_id(book_id)

    def update_book(self, book_id, updated_book):
        return self.book_repository.update(book_id, updated_book)

    def delete_book(self, book_id):
        self.book_repository.delete(book_id)

