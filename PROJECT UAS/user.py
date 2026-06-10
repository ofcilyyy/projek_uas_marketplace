from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, username, password, role):
        self.username = username
        self.__password = password  # Encapsulation (Private)
        self.role = role

    def check_password(self, input_password):
        return self.__password == input_password

    @abstractmethod
    def login(self, input_password):
        """Abstraction method untuk proses login"""
        pass


class Admin(User):  # Inheritance
    def __init__(self, username, password):
        super().__init__(username, password, "Admin")

    def login(self, input_password):  # Method Override
        if self.check_password(input_password):
            print(f"\n[SUKSES] Admin '{self.username}' berhasil masuk ke sistem.")
            return True
        print("\n[GAGAL] Password Admin salah.")
        return False


class Customer(User):  # Inheritance & Subtyping
    def __init__(self, username, password):
        super().__init__(username, password, "Customer")
        self.cart = []  # Relationship (Agregasi dengan Product)

    def login(self, input_password):  # Method Override
        if self.check_password(input_password):
            print(f"\n[SUKSES] Customer '{self.username}' berhasil masuk ke sistem.")
            return True
        print("\n[GAGAL] Password Customer salah.")
        return False
