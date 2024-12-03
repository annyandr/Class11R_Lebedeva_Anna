import csv
import json
from datetime import datetime


class Note:
    def __init__(self, id: int, title: str, content: str, timestamp: str):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = timestamp

    @staticmethod
    def menu():
        while True:
            print("Управление заметками:")
            print("1. Создать заметку")
            print("2. Просмотреть заметки")
            print("3. Просмотреть подробности заметки")
            print("4. Редактировать заметку")
            print("5. Удалить заметку")
            print("6. Назад")

            choice = input("Введите номер действия: ")

            if choice == "1":
                title = input("Введите заголовок заметки: ")
                content = input("Введите содержимое заметки: ")
                Note.create_note(title, content)
            elif choice == "2":
                Note.list_notes()
            elif choice == "3":
                note_id = int(input("Введите ID заметки: "))
                Note.view_note(note_id)
            elif choice == "4":
                note_id = int(input("Введите ID заметки для редактирования: "))
                new_title = input("Введите новый заголовок: ")
                new_content = input("Введите новое содержимое: ")
                Note.edit_note(note_id, new_title, new_content)
            elif choice == "5":
                note_id = int(input("Введите ID заметки для удаления: "))
                Note.delete_note(note_id)
            elif choice == "6":
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    @staticmethod
    def load_notes():
        try:
            with open("notes.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def save_notes(notes):
        with open("notes.json", "w") as file:
            json.dump(notes, file, indent=4)

    @staticmethod
    def create_note(title: str, content: str):
        timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        notes = Note.load_notes()
        new_id = len(notes) + 1
        note = Note(new_id, title, content, timestamp)
        notes.append(note.__dict__)
        Note.save_notes(notes)

    @staticmethod
    def list_notes():
        notes = Note.load_notes()
        for note in notes:
            print(f'ID: {note["id"]}, Title: {note["title"]}, Timestamp: {note["timestamp"]}')

    @staticmethod
    def view_note(id: int):
        notes = Note.load_notes()
        for note in notes:
            if note["id"] == id:
                print(f'Title: {note["title"]}\nContent: {note["content"]}\nTimestamp: {note["timestamp"]}')

    @staticmethod
    def edit_note(id: int, new_title: str, new_content: str):
        notes = Note.load_notes()
        for note in notes:
            if note["id"] == id:
                note["title"] = new_title
                note["content"] = new_content
                note["timestamp"] = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        Note.save_notes(notes)

    @staticmethod
    def delete_note(id: int):
        notes = Note.load_notes()
        notes = [note for note in notes if note["id"] != id]
        Note.save_notes(notes)


class Task:
    def __init__(self, id: int, title: str, description: str, done: bool, priority: str, due_date: str):
        self.id = id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date

    @staticmethod
    def menu():
        pass


class Contact:
    def __init__(self, id: int, name: str, phone: str, email: str):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    @staticmethod
    def menu():
        pass


class FinanceRecord:
    def __init__(self, id: int, amount: float, category: str, date: str, description: str):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    @staticmethod
    def menu():
        pass


class CSVHandler:
    @staticmethod
    def read_csv(file_path: str):
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            print(f"Файл {file_path} не найден.")
            return []

    @staticmethod
    def write_csv(file_path: str, data: list):
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            if data:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)


def calculator():
    while True:
        print("\nКалькулятор:")
        expression = input('Введите выражение или "q" для выхода: ')

        if expression.lower() == "q":
            break

        try:
            result = eval(expression)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")


def menu():
    while True:
        print("\nДобро пожаловать в Персональный помощник!")
        print("1. Управление заметками")
        print("2. Управление задачами")
        print("3. Управление контактами")
        print("4. Управление финансовыми записями")
        print("5. Калькулятор")
        print("6. Выход")

        choice = input("Введите номер действия: ")

        if choice == "1":
            Note.menu()
        elif choice == "2":
            Task.menu()
        elif choice == "3":
            Contact.menu()
        elif choice == "4":
            FinanceRecord.menu()
        elif choice == "5":
            calculator()
        elif choice == "6":
            print("Завершил работу.")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    menu()
