# Create list to hold inventory items
inventory = []


# Create the main menu
def display_menu():
    print("\n--- Inventory Management System ---")
    print("1. Add New Inventory")
    print("2. Update Existing Inventory")
    print("3. Remove Inventory")
    print("4. Search Inventory")
    print("5. Summary of Inventory")
    print("6. Exit")


# Check inventory stock levels and display low stock alert if item quantity is below the threshold amount
def check_stock_levels():
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


# Add a new inventory item and details
def add_inventory():
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


# Update the quantity of an existing inventory item
def update_inventory():
    print("\n--- Update Existing Inventory ---")

    name = input("Enter the item name to update: ").strip()

    for item in inventory:
        if name.lower() in item["name"].lower():
            item["quantity"] = int(input("Enter new quantity: "))

            print("Database updated. Item updated successfully.")
            check_stock_levels()
            return

    print("Item not found.")


# Remove an inventory item
def remove_inventory():
    print("\n--- Remove Inventory ---")

    name = input("Enter the item name to remove: ").strip()

    for item in inventory:
        if name.lower() in item["name"].lower():
            inventory.remove(item)

            print("Item removed from inventory.")
            print("Database updated.")
            check_stock_levels()
            return

    print("Item not found.")


# Search for an inventory item and display item details
def search_inventory():
    print("\n--- Search Inventory ---")

    name = input("Enter item name to search: ").strip()

    for item in inventory:
        if name.lower() in item["name"].lower():
            print("\nItem Found:")
            print(f"Name: {item['name']}")
            print(f"Quantity: {item['quantity']}")
            print(f"Low Stock Threshold: {item['threshold']}")
            return

    print("Item not found.")


# Display inventory summary and item details
def inventory_summary():
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


# Main program function
def main():
    print("Start")
    print("User logs into system")

    user_exists = True #the user is logged into the system
    #loop through menu options until user exits
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

#call the function
main()