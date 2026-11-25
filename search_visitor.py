def search_token(waiting_queue, completed_queue): 
    print()
    print("[SEARCH TOKEN]".center(50,"-"))


    search = input("Enter Token Number: ")
    print("-" * 50)
    found = False
    
    for visitor in waiting_queue:
        if str(visitor[0]) == search:
            print("Token Number:",visitor[0])
            print("Visitor Name:", visitor[1])
            print("Service Type:", visitor[2])
            print(f"Status: Waiting, Number = {waiting_queue.index(visitor)+1}")
            print()
            found = True
            break
        else: pass

    for visitor in completed_queue:
        if str(visitor[0]) == search:
            print("Token Number :",visitor[0])
            print("Visitor Name:", visitor[1])
            print("Service Type :", visitor[2])
            print("Status: Completed")
            print()
            found = True
            break

    if found ==False:
        print("Visitor Not Found")
        print()
