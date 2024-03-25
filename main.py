class HotelOrder:
    """
    Реалізує клас для опису замовлення готелю.
    """

    def __init__(self, client_name: str, room_type: str, days_stay: int):
        """
        Ініціалізація екземпляра класу HotelOrder.

        Аргументи:
            client_name: Ім'я клієнта.
            room_type: Тип кімнати.
            days_stay: Кількість днів проживання.
        """
        self.client_name = client_name
        self.room_type = room_type
        self.days_stay = days_stay
        self._cost = self._calculate_cost()

    def _calculate_cost(self):
        """
        Розраховує загальну вартість проживання.

        Повертає:
            Загальна вартість проживання.
        """
        room_prices = {
            "Standard": 100,
            "Luxury": 200,
            "Apartment": 300,
        }
        return room_prices[self.room_type] * self.days_stay

    def add_order(self):
        """
        Додає нове замовлення.

        """
        orders_db = {}
        orders_db[self.client_name] = {
            "room_type": self.room_type,
            "days_stay": self.days_stay,
            "cost": self._cost,
        }
        print(f"Замовлення для {self.client_name} успішно додано!")

    def change_room_type(self, new_room_type: str):
        """
        Змінює тип кімнати для замовлення.

        Аргументи:
            new_room_type: Новий тип кімнати.
        """
        self.room_type = new_room_type
        self._cost = self._calculate_cost()

    def change_days_stay(self, new_days_stay: int):
        """
        Змінює кількість днів проживання для замовлення.

        Аргументи:
            new_days_stay: Нова кількість днів проживання.
        """
        self.days_stay = new_days_stay
        self._cost = self._calculate_cost()

    def cancel_order(self):
        """
        Видаляє замовлення.

        """
        orders_db = {}
        if self.client_name in orders_db:
            del orders_db[self.client_name]
            print(f"Замовлення для {self.client_name} успішно видалено!")
        else:
            print(f"Замовлення для {self.client_name} не знайдено!")

    @property
    def cost(self):
        """
        Отримання загальної вартості проживання.

        Повертає:
            Загальна вартість проживання.
        """
        return self._cost


order1 = HotelOrder("Ivan", "Standard", 3)

print(f"Вартість замовлення: {order1.cost}")

order1.change_room_type("Luxury")

print(f"Вартість замовлення після зміни типу кімнати: {order1.cost}")

order1.cancel_order()


# Завдання 2
class TaxiOrder:
    """
    Реалізує клас для опису замовлення таксі.
    """
    orders_db = {}

    def __init__(self, client_name, pickup_address, destination_address, car_type):
        """
        Ініціалізація екземпляра класу TaxiOrder.

        Аргументи:
            client_name: Ім'я клієнта.
            pickup_address: Адреса забирання.
            destination_address: Адреса призначення.
            car_type: Тип автомобіля.
        """
        self.client_name = client_name
        self.pickup_address = pickup_address
        self.destination_address = destination_address
        self.car_type = car_type
        self.__cost = self.__calculate_cost()

    def __calculate_cost(self):
        """
        Розраховує загальну вартість поїздки.

        Повертає:
            Загальна вартість поїздки.
        """
        base_prices = {
            "economy": 10,
            "comfort": 15,
            "business": 20,
        }
        return base_prices[self.car_type]

    def add_order(self):
        """
        Додає нове замовлення.

        """
        TaxiOrder.orders_db[self.client_name] = {
            "pickup_address": self.pickup_address,
            "destination_address": self.destination_address,
            "car_type": self.car_type,
            "cost": self.__cost,
        }
        print(f"Замовлення для {self.client_name} успішно додано!")

    def change_address(self, new_pickup_address, new_destination_address):
        """
        Змінює адресу замовлення.

        Аргументи:
            new_pickup_address: Нова адреса забирання.
            new_destination_address: Нова адреса призначення.
        """
        self.pickup_address = new_pickup_address
        self.destination_address = new_destination_address
        self.__cost = self.__calculate_cost()

    def change_car_type(self, new_car_type):
        """
        Змінює тип автомобіля для замовлення.

        Аргументи:
            new_car_type: Новий тип автомобіля.
        """
        self.car_type = new_car_type
        self.__cost = self.__calculate_cost()

    def cancel_order(self):
        """
        Видаляє замовлення.

        """
        if self.client_name in TaxiOrder.orders_db:
            del TaxiOrder.orders_db[self.client_name]
            print(f"Замовлення для {self.client_name} успішно видалено!")
        else:
            print(f"Замовлення для {self.client_name} не знайдено!")


order1 = TaxiOrder("Ivan", "Lviv", "Kyiv", "economy")

print(f"Вартість замовлення: {order1._TaxiOrder__cost}")

order1.change_car_type("business")

print(f"Вартість замовлення після зміни типу автомобіля: {order1._TaxiOrder__cost}")

order1.cancel_order()


