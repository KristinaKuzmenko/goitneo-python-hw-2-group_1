from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name is a required field.")
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Invalid number format.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        if phone not in [p.value for p in self.phones]:
            self.phones.append(Phone(phone))

    def edit_phone(self, phone, new_phone):
        for i, p in enumerate(self.phones):
            if p.value == phone:
                self.phones[i] = Phone(new_phone)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def find_phone(self, phone):
        return next((p.value for p in self.phones if p.value == phone), None)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        self.data.pop(name, None)
