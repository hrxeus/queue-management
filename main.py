import add_new_visitor as add
from search_visitor import search_token
from serve import serve_next_visitor


while True:
    print("-" * 50)
    print("Smart Queue Management System".center(50, "-"))
    print("-" * 50)
    print("1. Add New Visitor\n2. View Waiting Queue\n3. Serve Next Visitor\n4. Search Token\n5. Completed Services\n6. Exit")
    print("-" * 50)

    choice = input("Enter your choice : ").strip()
    print("-" * 50)
    if choice == "1":
        add.add_new_visitor()
    elif choice == "2":
        display_visitors(add.waiting_queue, "Waiting Queue", "No visitors are waiting.")
    elif choice == "3":
        serve_next_visitor(add.waiting_queue)
    elif choice == "4":
        search_token(add.waiting_queue)
    elif choice == "5":
        display_visitors(add.completed_services, "Completed Services", "No completed services yet.")
    elif choice == "6":
        print("Thank You".center(50, "-"))
        break
    else:
        print("Please select correct option!!")
