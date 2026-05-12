from flask import Flask, request, jsonify
from db import create_tables
from services.library_service import LibraryService
from models.book import Book

app = Flask(__name__)
service = LibraryService()
create_tables()

@app.route("/books", methods=["POST"])
def add_book():
    data = request.json 
    book = Book(
    title=data["title"],
    author=data["author"],
    year=data["year"],
    available=data.get("available",1)
    )
    
    service.add_book(book)
    
    return jsonify({"message":"Book added successfully"}), 201
    
    
@app.route("/books", methods=["GET"])
def get_books():
    page = int(request.args.get("page",1))
    limit = int(request.args.get("limit", 5))
    year = request.args.get("year")
    available = request.args.get("available")
    
    year = int(year) if year else None 
    available = int(available) if available else None 
    
    books = service.get_books_paginated(page, limit, year, available)
    result = []
    for b in books:
        result.append({
        "id" : b.id,
        "title" : b.title,
        "author" : b.author,
        "year" : b.year,
        "available" : b.available
        })
        
    return jsonify(result)
        
        
@app.route("/books/search",methods=["GET"])
def search_books():
    keyword = request.args.get("q","")
    books = service.search_books(keyword)
    result = []
    for b in books:
       result.append({
        "id" : b.id,
        "title" : b.title,
        "author" : b.author,
        "year" : b.year,
        "available" : b.available
        })
        
    return jsonify(result)
    
    
    
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.json
    
    service.update_book(
    book_id,
    data["title"],
    data["author"],
    data["year"]
    )
    
    return jsonify({"message":"book updated"})
    
    
@app.route("/books/<int:book_id>/availability", methods=["PATCH"])
def update_availability(book_id):
    data = request.json
    service.update_availability(book_id, data["available"])
    return jsonify({"message":"availability updated"})
    
    
    
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    service.delete_book(book_id)
    return jsonify({"message":"Book deleted"})
    
    
if __name__ == "__main__":
    app.run(debug=True)