waiting_queue = []
token = 0
def add_new_visitor():
    print()
    print("[ADDING NEW VISITOR]".center(50, "-"))

    while True:
        name = input("Visitors Name: ").strip()
        if name:
            break
        else: print("Please enter a Name")
    a_services = ('Fee Payment Enquiry', 'Hall Ticket Issues', 'Admission Enquiry', 'Scholarship Assistance','Library Card','Other queries')
    print("Available Services : ")
    for i in range(len(a_services)):
        print(f"{i+1}. a_services[i]")
    while True:
        v_service_type = input("Service Type : ")
        if v_service_type.isdecimal():
            v_service_type = int(v_service_type)
            if v_service_type > 6 or v_service_type == 0:
                print("Please select correct option!!")
                continue
            else:
                break

    while True:
        priority = input("Does visitor have priority(Yes/No): ")
        priority = priority.lower().strip()

        if priority == 'yes' or priority == 'no':
            break
        else:
            print("Please select Yes/No!!")

    print("-" * 50)
    global token 
    token += 1
    visitor_details = [token, name, a_services[v_service_type - 1], priority]
    waiting_queue.append(visitor_details)
    print(f"Token number = {token}, please wait!")
    print("-" * 50)
    print()
    waiting_queue.sort(key=lambda visitor: visitor[3] == "no")
     

    
