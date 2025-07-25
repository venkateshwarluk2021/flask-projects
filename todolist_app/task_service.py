from db import get_connection
from task import Task

def add_task(title, description, deadline, completed=False):
    database = get_connection()
    cursor = database.cursor()
    cursor.execute("""INSERT INTO tasks (title, description, deadline, completed) VALUES (?,?,?,?) """,
                   (title, description, deadline, int(completed)))
    database.commit()
    database.close()


def get_all_tasks():
    database = get_connection()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    database.close()
    return [Task(row["id"], row["title"], row["description"], row["deadline"], bool(row["completed"])) for row in rows]

def get_task_by_id(task_id):
    database = get_connection()
    cursor = database.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()
    database.close()
    if row:
        return Task(row["id"], row["title"], row["description"], row["deadline"], bool(row["completed"]))
    return None

def update_task(task_id, title, description, deadline, completed):
    database = get_connection()
    cursor = database.cursor()
    cursor.execute("""UPDATE tasks SET title=? , description=?, deadline=?, completed=?
WHERE id=?""",(title, description, deadline, int(completed), task_id))
    database.commit()
    database.close()

def delete_task(task_id):
    database = get_connection()
    cursor = database.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?",(task_id,))
    database.commit()
    database.close()
    

