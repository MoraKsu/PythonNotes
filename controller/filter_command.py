class FilterCommand:
    def __init__(self, note_manager):
        self.note_manager = note_manager

    def execute(self):
        start_date = input("Введите начальную дату фильтрации (гггг-мм-дд): ")
        end_date = input("Введите конечную дату фильтрации (гггг-мм-дд): ")
        filtered_notes = self.note_manager.filter_notes_by_date(start_date, end_date)
        if filtered_notes:
            print("Результаты фильтрации:")
            for note in filtered_notes:
                print(f"Идентификатор: {note.note_id}")
                print(f"Заголовок: {note.title}")
                print(f"Тело: {note.body}")
                print(f"Дата/время: {note.timestamp}")
                print("-" * 20)
        else:
            print("Заметки не найдены.")