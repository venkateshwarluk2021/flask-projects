import pytest
from bookmark_manager import Bookmark, BookmarkManager

def test_add_and_list_bookmarks():
    manager = BookmarkManager()
    bm = Bookmark("https://example.com", "Example Site", "Some notes", ["example"])
    manager.add_bookmark(bm)

    bookmarks = manager.list_bookmarks()
    assert len(bookmarks) == 1
    assert bookmarks[0] == bm


def test_remove_existing_bookmark():
    manager = BookmarkManager()
    bm = Bookmark("https://example.com", "Example Site")
    manager.add_bookmark(bm)
    removed = manager.remove_bookmark("https://example.com")
    assert removed is True
    assert len(manager.list_bookmarks()) == 0

def test_remove_nonexisting_bookmark():
    manager = BookmarkManager()
    bm = Bookmark("https://example.com", "Example Site")
    manager.add_bookmark(bm)

    removed = manager.remove_bookmark("https://notfound.com")
    assert removed is False
    assert len(manager.list_bookmarks()) == 1

def test_find_bookmarks_by_title():
    manager = BookmarkManager()
    bm1 = Bookmark("https://site.com", "Python Site")
    bm2 = Bookmark("https://other.com", "Flask Docs")
    manager.add_bookmark(bm1)
    manager.add_bookmark(bm2)

    results = manager.find_bookmarks("Flask")
    assert len(results) == 1
    assert results[0] == bm2


def test_find_bookmarks_by_notes():
    manager = BookmarkManager()
    bm1 = Bookmark("https://site.com", "Title1", "Learn Flask")
    bm2 = Bookmark("https://other.com", "Title2", "Other notes")
    manager.add_bookmark(bm1)
    manager.add_bookmark(bm2)

    results = manager.find_bookmarks("flask")
    assert len(results) == 1
    assert results[0] == bm1

    
