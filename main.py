

class User:
    name = ""
    surname = ""
    age = 0
    email = ""

    def __init__(self, name, surname, age, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
    def set(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def printAll(self):
        print(f"Пользователь: {self.name}, его возраст {self.age}")


admin = User("Admin", "Marley", 21, "admin@gmail.com")
admin.printAll()

bob = User("Bob", "Marley", 18, "bob@gmail.com")
bob.printAll()

print('Hello')

