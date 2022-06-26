class Users:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance
    def __str__(self):
        return f"Users:{self.name} {self.surname},{self.city}.Баланс:{self.balance} руб."
    def get_guest(self):
        return f"Users:{self.name} {self.surname},{self.city}."
user_1 = Users("Иван", "Петров", "Москва", 50)
user_2 = Users("Сергей", "Сидоров","Челябинск", 100)
guest_list = [user_1, user_2]
for guest in guest_list:
    print(guest.get_guest())