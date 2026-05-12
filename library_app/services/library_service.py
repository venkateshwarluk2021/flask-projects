from db import get_connection
from models.book import Book

class LibraryService:
    
    def add_book(self, book: Book):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
        INSERT INTO books(title, author, year, available)
        VALUES (?,?,?,?)
        """, (book.title, book.author, book.year, book.available))
        
        conn.commit()
        conn.close()
        
        
    def get_all_books(self):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM books")
        rows = cursor.fetchall()
        
        conn.close()
        return [Book(row[1], row[2], row[3], row[4], row[0]) for row in rows]
        
    def search_books(self, keyword):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
        SELECT * FROM books
        WHERE title LIKE ? OR author LIKE ?
        """, (f"%{keyword}%",f"%{keyword}%"))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [Book(row[1], row[2], row[3], row[4], row[0]) for row in rows]
        
        
    def delete_book(self, book_id):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM books WHERE id=?",(book_id,))
        conn.commit()
        conn.close()
        
    def update_availability(self, book_id, status):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
        UPDATE books SET available=?
        WHERE id=?
        """, (status, book_id))
        
        conn.commit()
        conn.close()
        
        
    def get_books_paginated(self, page=1, limit=5, year=None, available=None):
        conn = get_connection()
        cursor = conn.cursor()
        
        query = "SELECT * FROM books WHERE 1=1"
        params = []
        
        if year:
            query += " AND year=?"
            params.append(year)
            
        if available is not None:
            query += " AND available=?"
            params.append(available)
            
        offset = (page-1)*limit
        query += " LIMIT ? OFFSET ?"
        params.extend([limit,offset])
        
        cursor.execute(query, params)
        rows = cursor.fetchall()
        
        conn.close()
        
        return [Book(row[1],row[2],row[3],row[4],row[0]) for row in rows]
        
        
    def update_book(self,book_id, title, author, year):
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
        UPDATE books
        SET title=?, author=?, year=?
        WHERE id=?
        """,(title, author, year, book_id))
        
        conn.commit()
        conn.close()
        
        
    def get_total_books_count(self, year=None, available=None):
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT COUNT(*) FROM books WHERE 1=1"
        params = []
        if year:
            query += " AND year=?"
            params.append(year)
        if available is not None:
            query += " AND available=?"
            params.append(available)

        cursor.execute(query,params)
        count = cursor.fetchone()[0]

        conn.close()
        return count
        
        
