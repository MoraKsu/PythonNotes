from datetime import datetime


class Note:
    def __init__(self, note_id, title, body, timestamp=None):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.timestamp = timestamp if timestamp is not None else datetime.now()

    def __dict__(self):
        return {
            'note_id': self.note_id,
            'title': self.title,
            'body': self.body,
            'timestamp': self.timestamp
        }

    def set_timestamp(self):
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')