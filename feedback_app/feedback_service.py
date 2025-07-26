import db
from feedback import Feedback

def create_table():
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("""
CREATE TABLE IF NOT EXISTS feedback(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
email TEXT NOT NULL,
message TEXT NOT NULL,
timestamp TEXT NOT NULL
)
""")
    conn.commit()
    conn.close()


def save_feedback(feedback:Feedback):
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("""
INSERT INTO feedback
(name, email, message, timestamp)
VALUES (?,?,?,?)""", feedback.to_tuple())
    conn.commit()
    conn.close()


def get_all_feedback():
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * from feedback ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_feedback(feedback_id):
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM feedback WHERE id = ?", (feedback_id,))
    conn.commit()
    conn.close()
