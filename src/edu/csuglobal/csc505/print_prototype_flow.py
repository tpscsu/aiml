#!/usr/bin/env python3
"""
Shopping List App Prototype Page Flow
"""


def print_prototype_flow():
    # Define the pages of the prototype with names and descriptions
    pages = [
        {"page_number": 1, "name": "Home Screen",
         "description": "Display existing shopping lists and 'Create New List' button."},
        {"page_number": 2, "name": "New List Screen", "description": "Enter a new shopping list name and save."},
        {"page_number": 3, "name": "Shopping List Detail Screen",
         "description": "View and add items to a shopping list."},
        {"page_number": 4, "name": "Edit Item Screen",
         "description": "Edit or update the details of an existing item."}
    ]

    total_pages = len(pages)
    print("Shopping List App Prototype")
    print("-" * 30)
    print(f"Total number of pages: {total_pages}\n")

    print("Page Flow Sequence:")
    for page in pages:
        print(f"Page {page['page_number']}: {page['name']}")
        print(f"  Description: {page['description']}")
        if page['page_number'] < total_pages:
            print("  Next ->")
    print("End of prototype flow.")


if __name__ == "__main__":
    print_prototype_flow()
