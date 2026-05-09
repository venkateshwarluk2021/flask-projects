class Book:
    def __init__(self, title, author, year, available=1, book_id=None):
        self.id = book_id 
        self.title = title 
        self.author = author 
        self.year = year 
        self.available = available 
        
        
    def __str__(self):
        status = "Available" if self.available else "Not Available"
        return f"{self.id} | {self.title} | {self.author} | {self.year} | {status}"