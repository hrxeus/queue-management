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

    while True:
        service = input("Service Needed: ").strip()
        if service:
            break
        else: print("Please enter a Service Type!")

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
    visitor_details = [token, name, service, priority]
    waiting_queue.append(visitor_details)
    print(f"Token number = {token}, please wait!")
    print("-" * 50)
    print()
    waiting_queue.sort(key=lambda visitor: visitor[3] == "no")
     

    
