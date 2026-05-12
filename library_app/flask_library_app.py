from flask import Flask, render_template, redirect, url_for, request, jsonify, flash
from db import create_tables
from services.library_service import LibraryService
from models.book import Book

app = Flask(__name__)
service = LibraryService()
create_tables()
app.secret_key = "secret123"

@app.route("/")
def home():
    page = int(request.args.get("page",1))
    limit = 5
    keyword = request.args.get("q")
    if keyword:
        books = service.search_books(keyword)
        total = len(books)
    else:
        books = service.get_books_paginated(page, limit)
        total = service.get_total_books_count()

    total_pages = ( total + limit -1 )//limit
    return render_template("index.html", books=books, page=page, total_pages=total_pages)
    
@app.route("/add", methods=["GET", "POST"])
def add_book_ui():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        year = int(request.form["year"])
        
        book = Book(title, author, year)
        service.add_book(book)
        flash("Book added successfully", "success")
        return redirect(url_for('home'))
        
    return render_template("add_book.html")

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit_book(book_id):
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        year = int(request.form["year"])

        service.update_book(book_id, title, author, year)
        return redirect(url_for('home'))

    # get - existing book
    books = service.get_all_books()
    book = next((b for b in books if b.id == book_id), None)

    return render_template("edit_book.html", book=book)

    
@app.route("/delete/<int:book_id>")
def delete_book_ui(book_id):
    service.delete_book(book_id)
    return redirect(url_for('home'))
    
    
@app.route("/toggle/<int:book_id>/<int:status>")
def toggle_status(book_id,status):
    service.update_availability(book_id, status)
    return redirect(url_for('home'))
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
