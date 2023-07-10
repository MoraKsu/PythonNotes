import json
import csv
from datetime import datetime


class NoteManager:
    def __init__(self):
        self.notes = []

    def add_note(self, note_id, title, body):
        note = {
            'Note ID': note_id,
            'Title': title,
            'Body': body,
            'Timestamp': str(datetime.now())
        }
        self.notes.append(note)

    def save_notes_to_csv(self):
        with open('notes.csv', 'w', newline='', encoding='utf-8-sig') as file:
            writer = csv.writer(file)
            writer.writerow(['Note ID', 'Title', 'Body', 'Timestamp'])
            for note in self.notes:
                writer.writerow([note.get('Note ID', ''), note.get('Title', ''), note.get('Body', ''), note.get('Timestamp', '')])

    def save_notes_to_json(self):
        with open('notes.json', 'w', encoding='utf-8-sig') as file:
            json.dump(self.notes, file, indent=4, cls=NoteEncoder)

    def edit_note(self, note_id, title, body):
        note = self.get_note_by_id(note_id)
        if note:
            note['Title'] = title
            note['Body'] = body

    def delete_note(self, note_id):
        note = self.get_note_by_id(note_id)
        if note:
            self.notes.remove(note)

    def filter_notes_by_date(self, start_date, end_date):
        filtered_notes = []
        for note in self.notes:
            note_timestamp = datetime.strptime(note['Timestamp'], '%Y-%m-%d %H:%M:%S.%f')
            if start_date.date() <= note_timestamp.date() <= end_date.date():
                filtered_notes.append(note)
        return filtered_notes

    def load_notes_from_json(self):
        try:
            with open("notes.json", 'r', encoding='utf-8-sig') as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            self.notes = []

    def load_notes_from_csv(self):
        with open("notes.csv", 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file, delimiter=',')
            next(reader)
            for row in reader:
                note_id, title, body, timestamp = row
                note = {
                    'Note ID': note_id,
                    'Title': title,
                    'Body': body,
                    'Timestamp': timestamp
                }
                self.notes.append(note)

    def get_note_by_id(self, note_id):
        for note in self.notes:
            if note.get('Note ID') == note_id:
                return note
        return None


class NoteEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S.%f')
        elif isinstance(obj, str):
            return obj.encode('utf-8').decode('utf-8-sig')
        return super().default(obj)

