class Human:
    default_name = "No name"
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Money: {self.__money}")
        print(f"House: {self.__house}")

    @staticmethod
    def default_info():
        print(f"Default Name: {Human.default_name}")
        print(f"Default Age: {Human.default_age}")

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house

    def earn_money(self):
        self.__money += 5000

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money < price:
            print("Not enough money!")
        else:
            self.__make_deal(house, price)


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        return self._price * (1 - discount)


class SmallHouse(House):
    def __init__(self, price):
        super().__init__(area=40, price=price)


Human.default_info()

human = Human(name="Sasha", age=27)
human.info()

house = SmallHouse(price=1500)
house_final_price = house.final_price(discount=0.05)
human.buy_house(house, discount=0.05)

human.earn_money()
human.buy_house(house, discount=0.05)

human.info()
