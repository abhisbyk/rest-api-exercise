from flask import Blueprint, request, jsonify
from app.services.book_service import BookService
from app.domain.dtos import BookDTO

book_blueprint = Blueprint('books', __name__)
book_service = BookService(None)  # Replace None with actual repository instance

@book_blueprint.route('/books', methods=['POST'])
def create_book():
    data = request.json
    book_dto = BookDTO(**data)
    book = book_service.create_book(book_dto)
    return jsonify(book.__dict__), 201

@book_blueprint.route('/books', methods=['GET'])
def get_books():
    books_dto = book_service.get_all_books()
    # Convert DTOs to JSON serializable format (usually via `__dict__`)
    return jsonify([book.__dict__ for book in books_dto]), 200

@book_blueprint.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = book_service.get_book_by_id(book_id)
    return jsonify(book.__dict__), 200 if book else 404

@book_blueprint.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    updated_book = book_service.update_book(book_id, data)
    return jsonify(updated_book.__dict__), 200

@book_blueprint.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book_service.delete_book(book_id)
    return '', 204

