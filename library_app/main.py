from db import create_tables
from services.library_service import LibraryService
from models.book import Book

service = LibraryService()

def menu():
    print("\nLibrary Service")
    print("1. add book")
    print("2. view books")
    print("3. search book")
    print("4. delete book")
    print("5. update availability")
    print("6. Paginated View")
    print("7. Update Book details")
    print("8. exit")
    
    
def main():
    create_tables()
    
    while True:
        menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            year = int(input("Year: "))
            
            book = Book(title, author, year)
            service.add_book(book)
            
            print("book added")
            
        elif choice == "2":
            books = service.get_all_books()
            for b in books:
                print(b)
                
        elif choice == "3":
            keyword = input("searching keyword: ")
            books = service.search_books(keyword)
            
            for b in books:
                print(b)
                
        elif choice == "4":
            book_id = int(input("Enter book id: "))
            service.delete_book(book_id)
            print("book deleted")
            
        elif choice == "5":
            book_id = int(input("Book ID: "))
            status = int(input("1=Available, 0=Not available: "))
            service.update_availability(book_id, status)
            
        elif choice == "6":
            page = int(input("Enter page number: "))
            limit = int(input("Enter limit (books per page) : "))
            
            year_filter = input("Filter by year (leave blank if none) : ")
            available_filter = input("Filter by availability (1/0 or blank): ")
            
            year_filter = int(year_filter) if year_filter else None 
            available_filter = int(available_filter) if available_filter else None 
            
            books = service.get_books_paginated(page, limit, year_filter, available_filter)
            
            if not books:
                print("No books found")
            else:
                for b in books:
                    print(b)
                    
                    
        elif choice == "7":
            book_id = int(input("Enter book id: "))
            title = input("New title: ")
            author = input("New author: ")
            year = int(input("New Year: "))
            
            service.update_book(book_id, title, author, year)
            print("Book updated")
            
        elif choice == "8":
            break 
            
        else:
            print("Invalid choic")
            
            
if __name__ == "__main__":
    main()

