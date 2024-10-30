class ItemToPurchase:
    def __init__(self, item_name="none", item_description="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")

    def print_item_description(self):
        print(f"{self.item_name}: {self.item_description}")


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
                item.print_item_description()


def get_valid_input(prompt, input_type):
    while True:
        try:
            return input_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")


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
            item_description = input("Enter the item description: ")
            item_price = get_valid_input("Enter the item price: ", float)
            item_quantity = get_valid_input("Enter the item quantity: ", int)
            item = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            cart.add_item(item)
            print(f"Added {item_quantity} of {item_name} to the cart.")

        elif choice == 'r':
            item_name = input("Enter name of item to remove: ")
            print("REMOVE ITEM FROM CART")
            cart.remove_item(item_name)

        elif choice == 'c':
            item_name = input("Enter the item name: ")
            item_quantity = get_valid_input("Enter the new quantity: ", int)
            item = ItemToPurchase(item_name=item_name, item_quantity=item_quantity)
            cart.modify_item(item)
            print(f"Updated {item_name}'s quantity to {item_quantity}.")

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

    print(f"Customer name: {customer_name}")
    print(f"Today's date: {current_date}")

    cart = ShoppingCart(customer_name, current_date)

    print_menu(cart)


if __name__ == "__main__":
    main()
