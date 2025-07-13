class Bookmark:
    def __init__(self, url, title, notes='', tags=None):
        self.url = url
        self.title = title
        self.notes = notes
        self.tags = tags if tags is not None else []

    def __str__(self):
        return f"[{self.title}] {self.url} (Notes:{self.notes})"


    def __eq__(self, other):
        if not isinstance(other, Bookmark):
            return False
        return (self.url == other.url and
                self.title == other.title and
                self.notes == other.notes and
                self.tags == other.tags)

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
            if (keyword.lower() in bm.title.lower() or keyword.lower() in bm.url.lower() or keyword.lower() in bm.notes.lower() or any(keyword.lower() in tag.lower() for tag in bm.tags)):
                results.append(bm)
        return results
    
    def delete_bookmark(self, url):
        self.bookmarks = [bm for bm in self.bookmarks if bm.url != url]
