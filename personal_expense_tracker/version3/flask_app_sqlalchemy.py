from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger
import os

app = Flask(__name__)

db_path = os.path.join(os.getcwd(), "data", "expenses.db")
os.makedirs(os.path.dirname(db_path), exist_ok=True)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
swagger = Swagger(app)

class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "amount": self.amount }


with app.app_context():
    db.create_all()

@app.route("/expenses", methods=["GET"])
def get_expenses():
     """
    Get all expenses
    ---
    responses:
      200:
        description: list of expenses
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              amount:
                type: number
    """

    expenses = Expense.query.all()
    return jsonify([e.to_dict() for e in expenses])

@app.route("/expenses", methods=["POST"])
def add_expense():
    """
    Add a new expense
    ---
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            amount:
              type: number
    responses:
      201:
        description: Expense created
    """

    data = request.json
    new_expense = Expense(name=data["name"], amount=data["amount"])
    db.session.add(new_expense)
    db.session.commit()
    return jsonify(new_expense.to_dict()), 201


@app.route("/expenses/<int:expense_id>", methods=["DELETE"])
def delete_expense(expense_id):
    """
    Delete an expense
    ---
    parameters:
      - in: path
        name: expense_id
        type: integer
        required: true
    responses:
      200:
        description: Expense deleted
    """

    expense = Expense.query.get_or_404(expense_id)
    db.session.delete(expense)
    db.session.commit()
    return jsonify({"message":"expense deleted"})

@app.route("/expenses/<int:expense_id>", methods=["PUT"])
def edit_expense(expense_id):
    """
    Edit an expense
    ---
    parameters:
      - in: path
        name: expense_id
        type: integer
        required: true
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            amount:
              type: number
    responses:
      200:
        description: Expense updated
    """

    expense = Expense.query.get_or_404(expense_id)
    data = request.json
    expense.name = data.get("name", expense.name)
    expense.amount = data.get("amount", expense.amount)
    db.session.commit()
    return jsonify(expense.to_dict())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
