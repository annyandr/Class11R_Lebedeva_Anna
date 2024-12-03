import json
import csv
from datetime import datetime
import textwrap

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
        while True:
            print("Управление задачами:")
            print("1. Создать задачу")
            print("2. Просмотреть задачи")
            print("3. Отметить задачу как выполненную")
            print("4. Редактировать задачу")
            print("5. Удалить задачу")
            print("6. Назад")

            choice = input("Введите номер действия: ")

            if choice == "1":
                title = input("Введите заголовок задачи: ")
                description = input("Введите описание задачи: ")
                priority = input("Введите приоритет (низкий, средний, высокий): ")
                due_date = input("Введите срок выполнения (ДД-ММ-ГГГГ): ")
                Task.create_task(title, description, priority, due_date)
            elif choice == "2":
                Task.list_tasks()
            elif choice == "3":
                task_id = int(input("Введите ID задачи для выполнения: "))
                Task.mark_task_done(task_id)
            elif choice == "4":
                task_id = int(input("Введите ID задачи для редактирования: "))
                new_title = input("Введите новый заголовок: ")
                new_description = input("Введите новое описание: ")
                new_priority = input("Введите новый приоритет: ")
                new_due_date = input("Введите новый срок выполнения: ")
                Task.edit_task(task_id, new_title, new_description, new_priority, new_due_date)
            elif choice == "5":
                task_id = int(input("Введите ID задачи для удаления: "))
                Task.delete_task(task_id)
            elif choice == "6":
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    @staticmethod
    def load_tasks():
        try:
            with open("tasks.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def save_tasks(tasks):
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)

    @staticmethod
    def create_task(title: str, description: str, priority: str, due_date: str):
        tasks = Task.load_tasks()
        new_id = len(tasks) + 1
        task = Task(new_id, title, description, False, priority, due_date)
        tasks.append(task.__dict__)
        Task.save_tasks(tasks)

    @staticmethod
    def list_tasks():
        tasks = Task.load_tasks()
        for task in tasks:
            status = "Выполнена" if task["done"] else "Не выполнена"
            print(f'ID: {task["id"]}, Title: {task["title"]}, Status: {status}, Priority: {task["priority"]}, Due Date: {task["due_date"]}')

    @staticmethod
    def mark_task_done(task_id: int):
        tasks = Task.load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                task["done"] = True
        Task.save_tasks(tasks)

    @staticmethod
    def edit_task(task_id: int, new_title: str, new_description: str, new_priority: str, new_due_date: str):
        tasks = Task.load_tasks()
        for task in tasks:
            if task["id"] == task_id:
                task["title"] = new_title
                task["description"] = new_description
                task["priority"] = new_priority
               task["due_date"] = new_due_date
        Task.save_tasks(tasks)

    @staticmethod
    def delete_task(task_id: int):
        tasks = Task.load_tasks()
        tasks = [task for task in tasks if task["id"] != task_id]
        Task.save_tasks(tasks)

class Contact:
    def __init__(self, id: int, name: str, phone: str, email: str):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    @staticmethod
    def menu():
        """Меню для управления контактами"""
        while True:
            print("Управление контактами:")
            print("1. Создать новый контакт")
            print("2. Просмотреть контакты")
            print("3. Поиск контакта")
            print("4. Редактировать контакт")
            print("5. Удалить контакт")
            print("6. Импорт контактов из CSV")
            print("7. Экспорт контактов в CSV")
            print("8. Назад")

            choice = input("Введите номер действия: ")

            if choice == "1":
                name = input("Введите имя контакта: ")
                phone = input("Введите телефон контакта: ")
                email = input("Введите email контакта: ")
                Contact.create_contact(name, phone, email)
            elif choice == "2":
                Contact.list_contacts()
            elif choice == "3":
                query = input("Введите имя или телефон для поиска: ")
                Contact.search_contact(query)
            elif choice == "4":
                contact_id = int(input("Введите ID контакта для редактирования: "))
                new_name = input("Введите новое имя: ")
                new_phone = input("Введите новый телефон: ")
                new_email = input("Введите новый email: ")
                Contact.edit_contact(contact_id, new_name, new_phone, new_email)
            elif choice == "5":
                contact_id = int(input("Введите ID контакта для удаления: "))
                Contact.delete_contact(contact_id)
            elif choice == "6":
                filename = input("Введите имя файла для импорта контактов: ")
                Contact.import_contacts_from_csv(filename)
            elif choice == "7":
                filename = input("Введите имя файла для экспорта контактов: ")
                Contact.export_contacts_to_csv(filename)
            elif choice == "8":
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    @staticmethod
    def load_contacts():
        """Загружает контакты из файла"""
        try:
            with open("contacts.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def save_contacts(contacts):
        """Сохраняет контакты в файл"""
        with open("contacts.json", "w") as file:
            json.dump(contacts, file, indent=4)

    @staticmethod
    def create_contact(name: str, phone: str, email: str):
        """Создает контакт и добавляет его в список"""
        contacts = Contact.load_contacts()
        new_id = len(contacts) + 1
        contact = Contact(new_id, name, phone, email)
        contacts.append(contact.__dict__)
        Contact.save_contacts(contacts)

    @staticmethod
    def list_contacts():
        """Выводит список всех контактов"""
        contacts = Contact.load_contacts()
        for contact in contacts:
            print(f'ID: {contact["id"]}, Name: {contact["name"]}, Phone: {contact["phone"]}, Email: {contact["email"]}')

    @staticmethod
    def search_contact(query: str):
        """Поиск контакта по имени или номеру телефона"""
        contacts = Contact.load_contacts()
        found_contacts = [contact for contact in contacts if query.lower() in contact["name"].lower() or query in contact["phone"]]
        if found_contacts:
            for contact in found_contacts:
                print(f'ID: {contact["id"]}, Name: {contact["name"]}, Phone: {contact["phone"]}, Email: {contact["email"]}')
        else:
            print("Контакт не найден.")

    @staticmethod
    def edit_contact(contact_id: int, new_name: str, new_phone: str, new_email: str):
        """Редактирование контакта"""
        contacts = Contact.load_contacts()
        for contact in contacts:
            if contact["id"] == contact_id:
                contact["name"] = new_name
                contact["phone"] = new_phone
                contact["email"] = new_email
        Contact.save_contacts(contacts)

    @staticmethod
    def delete_contact(contact_id: int):
        """Удаление контакта по ID"""
        contacts = Contact.load_contacts()
        contacts = [contact for contact in contacts if contact["id"] != contact_id]
        Contact.save_contacts(contacts)

    @staticmethod
    def import_contacts_from_csv(filename: str):
        """Импортирует контакты из CSV"""
        contacts = Contact.load_contacts()
        try:
            with open(filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    new_contact = Contact(int(row["id"]), row["name"], row["phone"], row["email"])
                    contacts.append(new_contact.__dict__)
            Contact.save_contacts(contacts)
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")

    @staticmethod
    def export_contacts_to_csv(filename: str):
        """Экспортирует контакты в CSV"""
        contacts = Contact.load_contacts()
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name", "phone", "email"])
            writer.writeheader()
            writer.writerows(contacts)

class FinanceRecord:
    def __init__(self, id: int, amount: float, category: str, date: str, description: str):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    @staticmethod
    def menu():
        """Меню управления финансовыми записями"""
        while True:
            print(textwrap.dedent("""
                \nУправление финансовыми записями:
                1. Добавить запись
                2. Просмотреть записи
                3. Сгенерировать отчёт
                4. Импорт записей из CSV
                5. Экспорт записей в CSV
                6. Назад
            """))
            choice = input("Введите номер действия: ").strip()

            if choice == "1":
                try:
                    amount = float(input("Введите сумму (доход положительный, расход отрицательный): "))
                    category = input("Введите категорию: ").strip()
                    date = input("Введите дату (ДД-ММ-ГГГГ): ").strip()
                    description = input("Введите описание: ").strip()
                    FinanceRecord.add_record(amount, category, date, description)
                except ValueError:
                    print("Ошибка ввода суммы. Попробуйте снова.")
            elif choice == "2":
                filter_date = input("Фильтр по дате (ДД-ММ-ГГГГ) или Enter для всех: ").strip()
                filter_category = input("Фильтр по категории или Enter для всех: ").strip()
                FinanceRecord.view_records(filter_date or None, filter_category or None)
            elif choice == "3":
                start_date = input("Начальная дата (ДД-ММ-ГГГГ): ").strip()
                end_date = input("Конечная дата (ДД-ММ-ГГГГ): ").strip()
                FinanceRecord.generate_report(start_date, end_date)
            elif choice == "4":
                filename = input("Введите имя файла для импорта: ").strip()
                FinanceRecord.import_records_from_csv(filename)
            elif choice == "5":
                filename = input("Введите имя файла для экспорта: ").strip()
                FinanceRecord.export_records_to_csv(filename)
            elif choice == "6":
                break
            else:
                print("Неверный выбор, попробуйте снова.")

    @staticmethod
    def load_records():
        """Загружает записи из JSON-файла."""
        try:
            with open("finance_records.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    @staticmethod
    def save_records(records):
        """Сохраняет записи в JSON-файл."""
        with open("finance_records.json", "w") as file:
            json.dump(records, file, indent=4)

    @staticmethod
    def add_record(amount, category, date, description):
        """Добавляет новую запись."""
        records = FinanceRecord.load_records()
        new_id = len(records) + 1
        record = FinanceRecord(new_id, amount, category, date, description)
        records.append(record.__dict__)
        FinanceRecord.save_records(records)

    @staticmethod
    def view_records(filter_date=None, filter_category=None):
        """Просмотр записей с фильтрацией."""
        records = FinanceRecord.load_records()
        if filter_date:
            records = [r for r in records if r["date"] == filter_date]
        if filter_category:
            records = [r for r in records if r["category"] == filter_category]
        
        for record in records:
            print(f"ID: {record['id']}, Сумма: {record['amount']}, Категория: {record['category']}, "
                  f"Дата: {record['date']}, Описание: {record['description']}")

    @staticmethod
    def generate_report(start_date, end_date):
        """Генерация отчёта за период."""
        records = FinanceRecord.load_records()
        start_date = datetime.strptime(start_date, "%d-%m-%Y")
        end_date = datetime.strptime(end_date, "%d-%m-%Y")
        
        filtered_records = [
            r for r in records 
            if start_date <= datetime.strptime(r["date"], "%d-%m-%Y") <= end_date
        ]
        total_income = sum(r["amount"] for r in filtered_records if r["amount"] > 0)
        total_expense = sum(r["amount"] for r in filtered_records if r["amount"] < 0)

        print(f"Отчёт с {start_date.strftime('%d-%m-%Y')} по {end_date.strftime('%d-%m-%Y')}")
        print(f"Доход: {total_income}")
        print(f"Расход: {abs(total_expense)}")
        print(f"Баланс: {total_income + total_expense}")

    @staticmethod
    def import_records_from_csv(filename):
        """Импорт записей из CSV."""
        records = FinanceRecord.load_records()
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                new_record = FinanceRecord(
                    int(row["id"]), float(row["amount"]), row["category"], row["date"], row["description"]
                )
                records.append(new_record.__dict__)
        FinanceRecord.save_records(records)

    @staticmethod
    def export_records_to_csv(filename):
        """Экспорт записей в CSV."""
        records = FinanceRecord.load_records()
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["id", "amount", "category", "date", "description"])
            writer.writeheader()
            writer.writerows(records)


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
