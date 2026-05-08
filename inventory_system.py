"""
Inventory Management System
Author: Shelese Jenkins

This program follows the inventory management flowsheet:
- User logs in
- Main menu displays
- User can add, update, remove, search, or summarize inventory
- Database is updated after inventory changes
- Stock levels are checked after updates
- Low stock alerts display when quantity is below threshold
"""

# This list acts as a simple in-memory database for inventory items.
inventory = []


def display_menu():
    """Display the main menu options to the user."""
    print("\n--- Inventory Management System ---")
    print("1. Add New Inventory")
    print("2. Update Existing Inventory")
    print("3. Remove Inventory")
    print("4. Search Inventory")
    print("5. Summary of Inventory")
    print("6. Exit")


def check_stock_levels():
    """
    Check each inventory item to see if its quantity is below
    the low-stock threshold.
    """
    low_stock_found = False

    for item in inventory:
        if item["quantity"] < item["threshold"]:
            low_stock_found = True
            print(
                f"LOW STOCK ALERT: {item['name']} has only "
                f"{item['quantity']} left. Threshold is {item['threshold']}."
            )

    if not low_stock_found:
        print("Stock levels are okay.")


def add_inventory():
    """Prompt the user to enter details for a new inventory item."""
    print("\n--- Add New Inventory ---")

    name = input("Enter inventory item name: ").strip()
    quantity = int(input("Enter quantity: "))
    threshold = int(input("Enter low stock threshold: "))

    item = {
        "name": name,
        "quantity": quantity,
        "threshold": threshold
    }

    inventory.append(item)

    print("Database updated. Item added successfully.")
    check_stock_levels()


def update_inventory():
    """Prompt the user to update an existing inventory item."""
    print("\n--- Update Existing Inventory ---")

    name = input("Enter the item name to update: ").strip()

    for item in inventory:
        if item["name"].lower() == name.lower():
            item["quantity"] = int(input("Enter new quantity: "))
            item["threshold"] = int(input("Enter new low stock threshold: "))

            print("Database updated. Item updated successfully.")
            check_stock_levels()
            return

    print("Item not found.")


def remove_inventory():
    """Prompt the user to remove an inventory item."""
    print("\n--- Remove Inventory ---")

    name = input("Enter the item name to remove: ").strip()

    for item in inventory:
        if item["name"].lower() == name.lower():
            inventory.remove(item)

            print("Item removed from inventory.")
            print("Database updated.")
            check_stock_levels()
            return

    print("Item not found.")


def search_inventory():
    """Prompt the user to search for an inventory item by name."""
    print("\n--- Search Inventory ---")

    name = input("Enter item name to search: ").strip()

    for item in inventory:
        if item["name"].lower() == name.lower():
            print("\nItem Found:")
            print(f"Name: {item['name']}")
            print(f"Quantity: {item['quantity']}")
            print(f"Low Stock Threshold: {item['threshold']}")
            return

    print("Item not found.")


def inventory_summary():
    """Display a summary of all inventory items."""
    print("\n--- Inventory Summary ---")

    if not inventory:
        print("No inventory items available.")
        return

    for item in inventory:
        print(
            f"Name: {item['name']} | "
            f"Quantity: {item['quantity']} | "
            f"Threshold: {item['threshold']}"
        )

    print(f"Total number of inventory items: {len(inventory)}")


def main():
    """
    Main program loop.
    The user stays in the system until they choose to exit.
    """
    print("Start")
    print("User logs into system")

    user_exists = True

    while user_exists:
        display_menu()
        choice = input("Select an action item: ").strip()

        if choice == "1":
            add_inventory()
        elif choice == "2":
            update_inventory()
        elif choice == "3":
            remove_inventory()
        elif choice == "4":
            search_inventory()
        elif choice == "5":
            inventory_summary()
        elif choice == "6":
            user_exists = False
            print("End")
        else:
            print("Invalid choice. Please select a number from 1 to 6.")

        if user_exists:
            input("\nPress Enter to return to the menu...")


# This ensures the program runs only when this file is executed directly.
if __name__ == "__main__":
    main()
