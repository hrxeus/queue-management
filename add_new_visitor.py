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
            if v_service_type > 4 or v_service_type == 0:
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
    
       
            