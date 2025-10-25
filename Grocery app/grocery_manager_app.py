my_list = []

def add_item(groceries):
    my_list.append(groceries)
    print(f"'{groceries}' added to the list.")
    return my_list


def remove_item(*groceries):
    if groceries in my_list:
        my_list.remove(groceries)
        print(f"'{groceries}' removed from the list.")
    else:
        print(f"'{groceries}' not found in the list.")
    return my_list


def show_available_items():
    if my_list:
        print("\nYour Grocery List:")
        for i, item in enumerate(my_list, start=1):
            print(f"{i}. {item}")
    else:
        print("Your grocery list is empty.")
