class SaveCommand:
    def __init__(self, note_manager):
        self.note_manager = note_manager

    def execute(self):
        filename = input("Введите имя файла для сохранения заметок: ")
        file_extension = input("Введите расширение файла (json или csv): ")
        if file_extension == "json":
            self.note_manager.save_notes_to_json(filename)
        elif file_extension == "csv":
            self.note_manager.save_notes_to_csv(filename)
        else:
            print("Неверное расширение файла. Сохранение не выполнено.")