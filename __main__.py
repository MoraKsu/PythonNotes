from view.console_app import ConsoleApp
from model.note_manager import NoteManager


def main():
    note_manager = NoteManager()
    app = ConsoleApp(note_manager)
    app.run()


if __name__ == "__main__":
    main()
