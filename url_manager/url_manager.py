class Bookmark:
    def __init__(self, url ,title, notes='', tags=None):
        self.url = url
        self.title = title
        self.notes = notes
        self.tags = tags if tags is not None else []

    def __str__(self):
        return f"[{self.title}] {self.url} (Notes: {self.notes})"

class BookmarkManager:
    def __init__(self):
        self.bookmarks = []

    def add_bookmark(self, bookmark):
        self.bookmarks.append(bookmark)

    def remove_bookmark(self, url):
        for bm in self.bookmarks:
            if bm.url == url:
                self.bookmarks.remove(bm)
                return True
        return False


    def list_bookmarks(self):
        return self.bookmarks

    def find_bookmarks(self, keyword):
        results = []
        for bm in self.bookmarks:
            if (keyword.lower() in bm.title.lower() or
                keyword.lower() in bm.url.lower() or
                keyword.lower() in bm.notes.lower()
                ):
                results.append(bm)
        return results


if __name__ == "__main__":
    manager = BookmarkManager()

    b1 = Bookmark("https://realpython.com", "Real Python", "Great tutorials", ["Python", "Tutorials"])
    b2 = Bookmark("https://flask.palletsprojects.com", "Flask Docs", "Flask official docs")

    manager.add_bookmark(b1)
    manager.add_bookmark(b2)

    print("All Bookmarks")
    for bm in manager.list_bookmarks():
        print(bm)

    print("\n Searching for flask")
    results = manager.find_bookmarks("flask")
    for bm in results:
        print(bm)

    manager.remove_bookmark("https://flask.palletsprojects.com")

    print("\nAfter Deletion")
    for bm in manager.list_bookmarks():
        print(bm)
        
    
