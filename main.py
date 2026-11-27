import add_new_visitor as add
from search_visitor import search_token
import serve
from display import display_visitors
from report import generate_reports


while True:
    print("-" * 50)
    print('|' + "Smart Queue Management System".center(48, " ") + '|')
    print("-" * 50)
    print("1. Add New Visitor\n2. View Waiting Queue\n3. Serve Next Visitor\n4. Search Token\n5. Completed Services\n6. Display Queue Report\n7. Exit")
    print("-" * 50)

    choice = input("Enter your choice : ").strip()
    print("-" * 50)
    if choice == "1":
        add.add_new_visitor()
    elif choice == "2":
        display_visitors(add.waiting_queue, "WAITING QUEUE")
    elif choice == "3":
        serve.serve_next_visitor(add.waiting_queue)
    elif choice == "4":
        search_token(add.waiting_queue, serve.completed_services)
    elif choice == "5":
        display_visitors(serve.completed_services, "COMPLETED SERVICES")
    elif choice == "6":
        generate_reports(add.waiting_queue, serve.completed_services)
    elif choice == "7":
        print("[THANK YOU]".center(50, "-"))
        break
    else:
        print("Please select correct option!!")
