from flask import Flask, render_template, request, redirect, url_for, flash
from bookmark_manager import Bookmark, BookmarkManager
from config import SECRET_KEY

app = Flask(__name__)
# Note: In production, use environment variables or a config file for secret keys.
app.secret_key = SECRET_KEY
manager = BookmarkManager()

@app.route("/")
def home():
    bookmarks = manager.list_bookmarks()
    return render_template("index.html", bookmarks=bookmarks)

@app.route("/add", methods=["GET","POST"])
def add_bookmark():
    if request.method=="POST":
        url = request.form["url"]
        title = request.form["title"]
        notes = request.form.get("notes","")
        tags = request.form.get("tags", "")
        tag_list = [t.strip() for t in tags.split(",")] if tags else []

        bm = Bookmark(url, title, notes, tag_list)
        manager.add_bookmark(bm)
        flash("Bookmark added successfully","success")
        return redirect(url_for("home"))

    return render_template("add.html")

@app.route("/search",methods=["GET","POST"])
def search():
    results = []
    keyword = ""
    if request.method == "POST":
        keyword = request.form["keyword"]
        results = manager.find_bookmarks(keyword)
    return render_template("search.html", keyword=keyword, results=results)

@app.route("/delete/<path:url>", methods=["POST"])
def delete_bookmark(url):
    manager.delete_bookmark(url)
    flash("Bookmark deleted successfully","danger")
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
