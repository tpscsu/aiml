import re


def normalize_string(s):
    """Removes extra spaces and makes the string lowercase for comparison."""
    return re.sub(r'\s+', ' ', s.strip()).lower()


def linear_search(database, target):
    target_normalized = normalize_string(target)

    for i, item in enumerate(database):
        item_name_normalized = normalize_string(item["name"])
        if item_name_normalized == target_normalized:
            return i
    return -1


# sample product database
marketplace = [
    {"id": 101, "name": "  Wireless    Mouse "},
    {"id": 102, "name": "USB-C Cable"},
    {"id": 103, "name": "Laptop Stand"},
    {"id": 104, "name": "Bluetooth    Keyboard"}
]

user_input = input("Enter the product name to search for: ")

search_result = linear_search(marketplace, user_input)

if search_result != -1:
    print(f"\nItem found at index {search_result}: {marketplace[search_result]}")
else:
    print(f"\nItem '{user_input.strip()}' not found in the marketplace.")
