from grocery_manager_app import *

while True:
    menu = """
========== GROCERY MANAGER APP ===========
1. Add items
2. Remove items
3. Show all items
4. Exit
"""
    print(menu)
    
    user = int(input("\nEnter your choice (1-4): "))

    match user:
        case 1:
            groceries = input("Enter item to add: ")
            add_item(groceries)

        case 2:
            groceries = input("Enter item to remove: ")
            remove_item(groceries)

        case 3:
            show_available_items()

        case 4:
            print(" Exiting Grocery Manager. Goodbye!")
            break

        case _:
            print(" Invalid choice! Please enter 1, 2, 3, or 4.")
