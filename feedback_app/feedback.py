from datetime import datetime

class Feedback:

    def __init__(self, name, email, message, timestamp=None):
        self.name = name
        self.email = email
        self.message = message
        self.timestamp = timestamp or datetime.now().strftime("%Y %m %d %H:%M:%S")

    def to_tuple(self):
        return (self.name, self.email, self.message, self.timestamp)
    
