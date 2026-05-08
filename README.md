# Inventory Management System

## Description
This Python program is an Inventory Management System created in Python. Users can add, up;date, remove, search, and view inventory items. The program also checks stock levels after inventory changes and displays a low-stock alert when an item's quantity is below the required threshold.

## Features
- Main menu display
- Add new inventory items
- Update existing inventory items
- Remove inventory items
- Search inventory by item name
- View inventory summary
- Check stock levels
- Display low-stock alerts
- Exit the system

## Files
- inventory_system.py - Main Python program
- README.md - Project documentation

## How to Run the Program
python inventory_system.py

## Program Flow
The program follows this general flow:

1. Start
2. User logs into the system
3. Main menu is displayed
4. User selects an action item
5. The selected inventory action is completed
6. Database is updated when needed
7. Stock levels are checked
8. Low-stock alerts are displayed if needed
9. User returns to the menu or exits
10. End

## Menu Options
1. Add New Inventory
2. Update Existing Inventory
3. Remove Inventory
4. Search Inventory
5. Summary of Inventory
6. Exit

## Notes
This version uses a Python list as a simple in-memory database. This means inventory data will reset when the program closes. 
A future improvement would be saving the inventory data to a file or database so the information remains available after the program ends.

## Author
Shelese Jenkins

## AI Usage Acknowledgement
This project was developed with assistance from ChatGPT/OpenAI for code structure, documentation, and program guidance. All code was reviewed, edited, and submitted by the author.
