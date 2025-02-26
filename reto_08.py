class MenuItem:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def set_price(self, value):
        self._price = value

    def calculate_total_price(self):
        return self._price


class Appetizer(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)


class MainCourse(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)


class Beverage(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

    def calculate_total_price(self, has_main_course):
        if has_main_course:
            return self.get_price() * 0.9  # 10% discount if there's a main course
        return self.get_price()


class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total_price(self):
        total = 0
        has_main_course = any(isinstance(item, MainCourse) for item in self.items)

        for item in self.items:
            if isinstance(item, Beverage):
                total += item.calculate_total_price(has_main_course)
            else:
                total += item.calculate_total_price()

        return total

    def display_order(self):
        print("Order Items:")
        for item in self.items:
            print(f"{item.get_name()}: ${item.get_price():.2f}")
        print(f"Total Price: ${self.calculate_total_price():.2f}")

    def __iter__(self):
        return OrderList(self)


class OrderList:
    def __init__(self, order):
        self._order = order
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._order.items):
            item = self._order.items[self._index]
            self._index += 1
            return item  # Return the actual MenuItem instance
        else:
            raise StopIteration


class Payment:
    def __init__(self, order):
        self.order = order

    def process_payment(self):
        total_price = self.order.calculate_total_price()
        print(f"Processing payment for total amount: ${total_price:.2f}")



if __name__ == "__main__":
    #menu items
    menu_items = [
        Appetizer("spagheti", 15.00),
        Appetizer("pan de ajo", 13.50),
        Appetizer("carbonara", 14.00),
        MainCourse("fetuccine", 15.00),
        MainCourse("Pasta Primavera", 12.00),
        MainCourse("fusiili", 20.00),
        Beverage("pepsi", 2.00),
        Beverage("vino", 10.00),
        Beverage("cerveza", 5.00),
        Beverage("Te helado", 3.00)
    ]

    # Create an order
    order = Order()
    order.add_item(menu_items[0])  
    order.add_item(menu_items[3])  
    order.add_item(menu_items[6])  
    order.add_item(menu_items[9]) 

    # Display the order
    order.display_order()

    # Using the OrderList to loop through items in the order
    print("\nIterating through order items:")
    for item in order:
        print(f"Item: {item.get_name()}, Price: ${item.get_price():.2f}")