class Users:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f"Users:{self.name} {self.surname},{self.city}.Баланс:{self.balance} руб."
users = Users("Иван", "Петров", "Москва", 50)
print(users)

