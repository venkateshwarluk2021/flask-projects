class Task:

    def __init__(self, id, title, description, deadline, completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.deadline = deadline
        self.completed = completed


    def mark_completed(self):
        self.completed = True

    def to_dict(self):
        return {
            'id':self.id,
            'title':self.title,
            'description':self.description,
            'deadline':self.deadline,
            'completed':self.completed
            }

    def __str__(self):
        return f"[{'done' if self.completed else 'pending' }] {self.title} - {self.deadline}"
