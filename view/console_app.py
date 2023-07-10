from datetime import datetime


class ConsoleApp:
    def __init__(self, note_manager):
        self.note_manager = note_manager

    def print_menu(self):
        print("Меню:")
        print("1. Просмотр всех заметок")
        print("2. Добавить заметку")
        print("3. Отредактировать заметку")
        print("4. Удалить заметку")
        print("5. Отфильтровать")
        print("6. Выход")

    def run(self):
        self.note_manager.load_notes_from_json()
        while True:
            self.print_menu()
            command = input("Введите номер команды: ")
            if command == "1":
                self.view_all_notes()
            elif command == "2":
                self.add_note()
                self.note_manager.save_notes_to_json()
                self.note_manager.save_notes_to_csv()
            elif command == "3":
                self.edit_note()
                self.note_manager.save_notes_to_json()
                self.note_manager.save_notes_to_csv()
            elif command == "4":
                self.delete_note()
                self.note_manager.save_notes_to_json()
                self.note_manager.save_notes_to_csv()
            elif command == "5":
                self.filter_notes()
            elif command == "6":
                self.note_manager.save_notes_to_csv()
                self.note_manager.save_notes_to_json()
                print("Программа завершена.")
                break
            else:
                print("Неверная команда. Пожалуйста, повторите ввод.")

    def view_all_notes(self):
        if self.note_manager.notes:
            print("Все заметки:")
            for note in self.note_manager.notes:
                print(f"Идентификатор: {note['Note ID']}")
                print(f"Заголовок: {note['Title']}")
                print(f"Тело: {note['Body']}")
                print(f"Дата/время: {note['Timestamp']}")
                print("-" * 20)
        else:
            print("Заметок не найдено.")

    def add_note(self):
        note_id = input("Введите идентификатор заметки: ")
        title = input("Введите заголовок заметки: ")
        body = input("Введите тело заметки: ")
        self.note_manager.add_note(note_id, title, body)
        print("Заметка успешно добавлена.")

    def edit_note(self):
        note_id = input("Введите идентификатор заметки для редактирования: ")
        title = input("Введите новый заголовок заметки: ")
        body = input("Введите новое тело заметки: ")
        self.note_manager.edit_note(note_id, title, body)
        print("Заметка успешно отредактирована.")

    def delete_note(self):
        note_id = input("Введите идентификатор заметки для удаления: ")
        self.note_manager.delete_note(note_id)
        print("Заметка успешно удалена.")

    def filter_notes(self):
        start_date = input("Введите начальную дату фильтрации (гггг-мм-дд): ")
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = input("Введите конечную дату фильтрации (гггг-мм-дд): ")
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        filtered_notes = self.note_manager.filter_notes_by_date(start_date, end_date)
        if filtered_notes:
            print("Результаты фильтрации:")
            for note in filtered_notes:
                print(f"Идентификатор: {note['Note ID']}")
                print(f"Заголовок: {note['Title']}")
                print(f"Тело: {note['Body']}")
                print(f"Дата/время: {note['Timestamp']}")
                print("-" * 20)
        else:
            print("Заметки не найдены.")


