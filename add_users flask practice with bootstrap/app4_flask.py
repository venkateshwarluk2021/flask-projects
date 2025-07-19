from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

@app.route("/users")
def list_users():
    return render_template("users.html", users=users)

@app.route("/users/create", methods=["GET","POST"])
def create_user():
    if request.method=="POST":
        new_id = max([u["id"] for u in users], default=0)+1
        name=request.form["name"]
        email=request.form["email"]
        users.append({"id":new_id,"name":name,"email":email})
        return redirect(url_for("list_users"))
    return render_template("user_form.html", action="Create", user=None)

@app.route("/users/edit/<int:user_id>", methods=["GET","POST"])
def edit_user(user_id):
    user=next((u for u in users if u["id"]==user_id),None)
    if not user:
        return "user not found", 404

    if request.method=="POST":
        user["name"]=request.form["name"]
        user["email"]=request.form["email"]
        return redirect(url_for("list_users"))
    return render_template("user_form.html", action="Edit",user=user)

@app.route("/users/delete/<int:user_id>")
def delete_user(user_id):
    global users
    users=[u for u in users if u["id"]!=user_id]
    return redirect(url_for("list_users"))


if __name__ == "__main__":
    app.run(debug=True)
           
