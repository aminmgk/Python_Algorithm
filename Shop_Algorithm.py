class Item:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price

class Device(Item):
    def __init__(self, code, name, price):
        super().__init__(code, name, price)

class SIMCard(Item):
    def __init__(self, code, name, price):
        super().__init__(code, name, price)

class Case(Item):
    def __init__(self, code, name, price):
        super().__init__(code, name, price)

class Charger(Item):
    def __init__(self, code, name, price):
        super().__init__(code, name, price)

class Shop:
    def __init__(self):
        self.devices = {
            "P1": Device("P1", "iPhone 14", 799.99),
            "P2": Device("P2", "Samsung Galaxy S22", 699.99),
            "T1": Device("T1", "iPad Pro", 999.99),
            "T2": Device("T2", "Samsung Galaxy Tab S8", 699.99)
        }
        self.sim_cards = {
            "SIM-FREE": SIMCard("SIM-FREE", "SIM-FREE", 0),
            "PAYG": SIMCard("PAYG", "PAYG", 19.99)
        }
        self.cases = {
            "STANDARD": Case("STANDARD", "Standard Case", 19.99),
            "LUXURY": Case("LUXURY", "Luxury Case", 39.99)
        }
        self.chargers = {
            "LIGHTNING": Charger("LIGHTNING", "Lightning Charger", 19.99),
            "USB-C": Charger("USB-C", "USB-C Charger", 14.99)
        }

    def get_valid_choice(self, prompt, choices):
        while True:
            choice = input(prompt).upper()
            if choice in choices:
                return choice
            print("Invalid choice. Please try again.")

    def task1(self):
        cart = []
        total = 0

        device_code = self.get_valid_choice("Enter the code for the device you want (P1, P2, T1, T2): ", self.devices.keys())
        device = self.devices[device_code]
        cart.append(device)
        total += device.price

        if isinstance(device, Device):
            sim_code = self.get_valid_choice("Choose a SIM type (SIM-FREE, PAYG): ", self.sim_cards.keys())
            sim_card = self.sim_cards[sim_code]
            cart.append(sim_card)
            total += sim_card.price

        case_code = self.get_valid_choice("Choose a case (STANDARD, LUXURY): ", self.cases.keys())
        case = self.cases[case_code]
        cart.append(case)
        total += case.price

        charger_codes = self.get_valid_choice("Choose chargers (LIGHTNING, USB-C, NONE): ", self.chargers.keys() | {"NONE"})
        if charger_codes != "NONE":
            for code in charger_codes.split(","):
                charger = self.chargers[code.strip()]
                cart.append(charger)
                total += charger.price

        print("\nItems in your cart:")
        for item in cart:
            print(f"- {item.name} (${item.price:.2f})")
        print(f"Total: ${total:.2f}")

        return cart, total

    def task2(self):
        total = 0
        cart = []

        while True:
            new_cart, new_total = self.task1()
            cart.extend(new_cart)
            total += new_total

            choice = self.get_valid_choice("\nWould you like to purchase another device? (Y/N): ", {"Y", "N"})
            if choice == "N":
                break

        print("\nTotal for all items:")
        for item in cart:
            print(f"- {item.name} (${item.price:.2f})")
        print(f"Total: ${total:.2f}")

        return cart, total

    def task3(self):
        cart, total = self.task2()
        discount = 0
        devices = [item for item in cart if isinstance(item, Device)]

        if len(devices) > 1:
            device_prices = [device.price for device in devices]
            discount = sum(price * 0.1 for price in device_prices[1:])
            total -= discount

        print("\nTotal with discount:")
        for item in cart:
            print(f"- {item.name} (${item.price:.2f})")
        print(f"Total: ${total:.2f}")
        print(f"Discount: ${discount:.2f}")

if __name__ == "__main__":
    shop = Shop()
    shop.task3()