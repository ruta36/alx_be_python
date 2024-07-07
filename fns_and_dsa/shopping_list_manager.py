def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            new_item = input("Enter the item to add: ").strip()
            if new_item:
                shopping_list.append(new_item)
                print(f"{new_item} added to the list.")
            else:
                print("Item name cannot be empty.")
        elif choice == '2':
            item_to_remove = input("Enter item to remove: ").strip()
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"{item_to_remove} removed from the list.")
            else:
                print(f"{item_to_remove} not found in the list.")
        elif choice == '3':
            if shopping_list:
                print("Shopping List:")
                for item in shopping_list:
                    print(item)
            else:
                print("The list is currently empty.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
