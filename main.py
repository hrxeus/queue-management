import add_new_visitor as add
import report as view

waiting_queue = []
completed_services = []
g_token = 0


while True:

    print("".center(50,"-"))
    print("Smart Queue Management System".center(50,"-"))
    print("".center(50,"-"))
    print("1. Add New Visitor\n2. View Waiting Queue\n3. Serve Next Visitor\n4. Search Token\n5. Completed Services\n7. Exit")
    print("".center(50,"-"))

    while True:
            menu_no = input("Enter your choice : ")
            if menu_no.isdecimal():
                menu_no = int(menu_no)
                break
            else:
                print("Please select correct option!!")
    print("".center(50,"-"))
    
    if(menu_no == 7):
        print("Thank You".center(50,"_"))
        break
    if(menu_no > 7):
        print("Please select correct option!!")
    if(menu_no == 1):
        add.add_new_visitor()
    if(menu_no == 2):
        view.generate_reports()
    