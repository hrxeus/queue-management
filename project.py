def add_new_visitor():
   
    print("=> Adding New Visitor".ljust(50,"-"))
    print("".center(50,"-"))
    a_services = ('Fee Payment Enquiry', 'Hall Ticket Issues', 'Admission Enquiry', 'Scholarship Assistance')
    print("Available Services : ")
    for i in range(len(a_services)):
        print(i+1,".",a_services[i])


    v_name = input("Name : ")
    v_service_type = eval(input("Service Type : "))

    print("Visitor Added Successfully".ljust(50,"-"))
    print("Token number : T{}".format(g_token))
    
    print("(Press '+' to Add Another Visitor)".center(50,"-"))
    x = eval(input())
    if(x == '+'):
        add_another = True
        print("x = + detected")
            





# Main Body.........................................................

waiting_queue = []
completed_services = []
g_token = 1
add_another = False


while True:

    print("".center(50,"-"))
    print("Smart Queue Management System".center(50,"-"))
    print("".center(50,"-"))

    

    print("1. Add New Visitor\n2. View Waiting Queue\n3. Serve Next Visitor\n4. Search Token\n5. Completed Services\n6. Queue Status\n7. Exit")
    print("".center(50,"-"))
    menu_no = eval(input("Enter your choice : "))
    print("".center(50,"-"))

    if(menu_no == 7):
        break
    if(menu_no == 1):
        add_new_visitor()
        g_token += 1
    
        
            
    
