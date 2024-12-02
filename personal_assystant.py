import csv

class Note:
    def __init__(self, id: int, title: str, content: str, timestamp: str):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = timestamp

    @staticmethod
    def menu():
        pass


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
    def write_csv(file_path: str, data: list[dict]):
        if not data:
            print("Нет данных для записи.")
            return
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


def calculator():
    while True:
        print("\nКалькулятор:")
        print('Введите арифметическое выражение или "q" для выхода.')
        expression = input("Введите выражение: ")

        if expression.lower() == "q":
            break

        try:
            result = eval(expression)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")


def menu():
    while True:
        print("Добро пожаловать в Персональный помощник!")
        print("Выберите действие:")
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
            print("Завершил работу")
            break
        else:
            print("Неверный выбор, попробуйте снова.")


if __name__ == "__main__":
    menu()
