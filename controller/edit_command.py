class EditCommand:
    def __init__(self, note_manager):
        self.note_manager = note_manager

    def execute(self):
        note_id = input("Введите идентификатор заметки для редактирования: ")
        title = input("Введите новый заголовок заметки: ")
        body = input("Введите новое тело заметки: ")
        self.note_manager.edit_note(note_id, title, body)
        print("Заметка успешно отредактирована.")