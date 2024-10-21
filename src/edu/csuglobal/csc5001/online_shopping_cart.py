class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        item_found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                item_found = True
                break
        if not item_found:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item):
        item_found = False
        for i in range(len(self.cart_items)):
            if self.cart_items[i].item_name == item.item_name:
                item_found = True
                # Update item if non-default values are provided
                if item.item_price != 0.0:
                    self.cart_items[i].item_price = item.item_price
                if item.item_quantity != 0:
                    self.cart_items[i].item_quantity = item.item_quantity
                break
        if not item_found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        total_quantity = 0
        for item in self.cart_items:
            total_quantity += item.item_quantity
        return total_quantity

    def get_cost_of_cart(self):
        total_cost = 0.0
        for item in self.cart_items:
            total_cost += item.item_price * item.item_quantity
        return total_cost

    def print_total(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            for item in self.cart_items:
                item.print_item_cost()
            print(f"\nTotal: ${self.get_cost_of_cart()}")

    def print_descriptions(self):
        if len(self.cart_items) == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
            print("Item Descriptions")
            for item in self.cart_items:
                print(f"{item.item_name}")


def print_menu(cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")

        if choice == 'a':
            item_name = input("Enter the item name: ")
            item_price = float(input("Enter the item price: "))
            item_quantity = int(input("Enter the item quantity: "))
            item = ItemToPurchase(item_name, item_price, item_quantity)
            cart.add_item(item)

        elif choice == 'r':
            item_name = input("Enter name of item to remove: ")
            cart.remove_item(item_name)

        elif choice == 'c':
            item_name = input("Enter the item name: ")
            item_price = float(input("Enter the new price (or leave as 0 for no change): "))
            item_quantity = int(input("Enter the new quantity (or leave as 0 for no change): "))
            item = ItemToPurchase(item_name, item_price, item_quantity)
            cart.modify_item(item)

        elif choice == 'i':
            cart.print_descriptions()

        elif choice == 'o':
            cart.print_total()

        elif choice == 'q':
            break

        else:
            print("Invalid option. Please try again.")


def main():
    customer_name = input("Enter customer's name: ")
    current_date = input("Enter today's date: ")

    cart = ShoppingCart(customer_name, current_date)

    print_menu(cart)


if __name__ == "__main__":
    main()
