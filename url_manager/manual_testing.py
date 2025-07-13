from bookmark_manager import Bookmark, BookmarkManager

def print_results(results):
    if not results:
        print("No Bookmarks found")
    else:
        for bm in results:
            print(bm)

def manual_test():
    manager = BookmarkManager()

    bm1 = Bookmark("https://site.com", "Python Site", "Python tutorials", ["programming", "language"])
    bm2 = Bookmark("https://flask.palletsprojects.com", "Flask Docs", "Web framework", ["flask", "web"])
    bm3 = Bookmark("https://github.com", "GitHub", "Code hosting", ["code", "repository"])

    manager.add_bookmark(bm1)
    manager.add_bookmark(bm2)
    manager.add_bookmark(bm3)

    print("=======print all Bookmarks=======")
    for bm in manager.list_bookmarks():
        print(bm)

    print("\n ======== search for keyword - Flask(title) ========")
    results = manager.find_bookmarks("flask")
    print_results(results)

    print("\n======search for keyword - framework (notes)======")
    results = manager.find_bookmarks("framework")
    print_results(results)

    print("\n=======search keyword code(tag/notees)==========")
    results = manager.find_bookmarks("code")
    print_results(results)

    print("\n===========search keyword nonexistent========")
    results = manager.find_bookmarks("nonexistinent")
    print_results(results)


if __name__ == "__main__":
    manual_test()
