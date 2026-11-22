def add_new_visitor():
   
    print("=> Adding New Visitor".ljust(50, "-"))
    print("".center(50))
    
    a_services = ('Fee Payment Enquiry', 'Hall Ticket Issues', 'Admission Enquiry', 'Scholarship Assistance')
    v_name = input("Visitors Name : ")
    print("Available Services : ")
    for i in range(len(a_services)):
        print("\t", i+1, ".", a_services[i])

    
    while True:
        v_service_type = input("Service Type : ")
        if v_service_type.isdecimal():
            v_service_type = int(v_service_type)
            if v_service_type > 4:
                print("Please select correct option!!")
                continue
            else:
                break
            
        else:
            print("Please select correct option!!")

    global g_token
    g_token += 1

    
    print("Visitor Added Successfully".ljust(50, "-"))
    
    visitor_details = (g_token, v_name, a_services[v_service_type - 1])
    print("Token number : T{}".format(g_token))
    
    waiting_queue.append(visitor_details)
    print(visitor_details)       
    
       
            





# Main Body.........................................................

waiting_queue = []
completed_services = []
g_token = 0
x = True


while True:

    print("".center(50,"-"))
    print("Smart Queue Management System".center(50,"-"))
    print("".center(50,"-"))
    print("1. Add New Visitor\n2. View Waiting Queue\n3. Serve Next Visitor\n4. Search Token\n5. Completed Services\n6. Queue Status\n7. Exit")
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
        add_new_visitor()
           