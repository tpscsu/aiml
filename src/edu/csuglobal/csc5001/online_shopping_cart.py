class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${total_cost}")


def main():
    # Ask for the number of items
    num_items = int(input("Enter the number of items: "))

    items = []  # List to hold ItemToPurchase objects
    total_cost = 0.0  # Track the total cost

    for i in range(num_items):
        print(f"\nItem {i + 1}")
        item_name = input("Enter the item name: ")
        item_price = float(input("Enter the item price: "))
        item_quantity = int(input("Enter the item quantity: "))

        item = ItemToPurchase(item_name, item_price, item_quantity)
        items.append(item)

    print("\nTOTAL COST")
    for item in items:
        item.print_item_cost()
        total_cost += item.item_price * item.item_quantity

    print(f"\nTotal: ${total_cost}")


if __name__ == "__main__":
    main()
