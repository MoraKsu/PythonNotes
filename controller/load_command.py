class LoadCommand:
    def __init__(self, note_manager):
        self.note_manager = note_manager

    def execute(self):
        filename = input("Введите имя файла для загрузки заметок: ")
        file_extension = input("Введите расширение файла (json или csv): ")
        if file_extension == "json":
            self.note_manager.load_notes_from_json(filename)
        elif file_extension == "csv":
            self.note_manager.load_notes_from_csv(filename)
        else:
            print("Неверное расширение файла. Загрузка не выполнена.")