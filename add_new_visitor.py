def add_new_visitor():
    print()
    print("Adding New Visitor")
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
            if v_service_type > 4 or v_service_type == 0:
                print("Please select correct option!!")
                continue
            else:
                break
            
        else:
            print("Please select correct option!!")
    while True:        
        v_priority = input("Does visitor have priority(Yes/No) : ")
        v_priority = v_priority.lower()

        if v_priority == 'yes' or v_priority == 'no':
            break
        else:
            print("Please select Yes/No !!")

    global g_token
    g_token += 1

    print()
    print("Visitor Added Successfully".ljust(50, "-"))
    
    visitor_details = [g_token, v_name, a_services[v_service_type - 1],v_priority]
    waiting_queue.append(visitor_details)

waiting_queue = []
completed_services = []
g_token = 0