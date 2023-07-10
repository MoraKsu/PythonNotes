class DeleteCommand:
    def __init__(self, note_manager):
        self.note_manager = note_manager

    def execute(self):
        note_id = input("Введите идентификатор заметки для удаления: ")
        self.note_manager.delete_note(note_id)
        print("Заметка успешно удалена.")