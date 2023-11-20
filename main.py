from collections import UserDict
from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit(): # Перевірка числа на 10 знаків
            raise ValueError("Phone number must be 10 digits")
        
        print(f'Number phone {value} has been add')
        super().__init__(value)

class Birthday(Field):
    def __init_(self, value):
        self.validate_date(value)
     
    def validate_date(self, value): # Перевірка на правильність дати
        try:
            day, month, year = map(int, value.split('/'))

            if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
                return super().__init__(value)
            else:
                raise ValueError('The date is not correct')
        except ValueError:
            raise ValueError('Incorrect date format(must be in day/month/year)')

class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday)

    def find_phone(self, phone): # Пошук телефона за нумером
        number_found = [num for num in self.phones if num.value == phone]
        return number_found[0] if number_found else None
    
    def remove_phone(self, phone): # Видаляємо нумер телефону
        self.phones = [num for num in self.phones if num.value != phone]
        print(f'Number phone {phone} has been delete')
    
    def edit_phone(self, old_phone, new_phone): # Заміна старого нумера на новий
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return
        raise ValueError(f'Phone number {old_phone} not found')
    
    def add_phone(self, phone): # Додавання нумеру
        self.phones.append(Phone(phone))
        
    def __str__(self): # Виводить контакт
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"
    
    def days_to_birthday(self):
        today = datetime.now()

        if self.birthday.value is not None:
            birth_day = self.birthday.value
            birth_day = datetime.strptime(birth_day, "%d/%m/%Y")

            next_birthday = datetime(today.year, birth_day.month, birth_day.day)

            if today > next_birthday:
                next_birthday = datetime(today.year + 1, birth_day.month, birth_day.day)

            days_until_birthday = (next_birthday - today).days

            return days_until_birthday
        else:
            print('Birthday is None')
    

class AddressBook(UserDict):
    def add_record(self, record): # Додавання контакту, ім'я це ключ
        self.data[record.name.value] = record
        print(f'Contact {record} has been add')
    
    def find(self, name): # Пошук контакта
        if name in self.data:
            return self.data[name]
        else:
            print(f'Name {name} is not found')
    
    def delete(self, name): # Видалення контакта
        if name in self.data:
            del self.data[name]
            print(f'The contact {name} has been deleted')

    def __iter__(self):
        self.current_number_data = 0
        self.current_data = list(self.data.values())
        return self
    
    def __next__(self):
        if self.current_number_data < len(self.current_data):
            notation = self.current_data[self.current_number_data]
            self.current_number_data += 1
            return notation
        else:
            StopIteration

if __name__ == "__main__":
    address_book = AddressBook()