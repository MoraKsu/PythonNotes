class AddCommand:
    def __init__(self, note_manager):
        self.note_manager = note_manager

    def execute(self):
        note_id = input("Введите идентификатор заметки: ")
        title = input("Введите заголовок заметки: ")
        body = input("Введите тело заметки: ")
        self.note_manager.add_note(note_id, title, body)
        print("Заметка успешно добавлена.")

