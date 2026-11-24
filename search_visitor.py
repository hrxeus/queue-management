def search_token(waiting_queue): 
    print("=> Search Token".ljust(50,"-"))
    print("".center(50,"-"))
    search = input("Enter Token Number (1,2,3...): ")
    found = False
    
    for visitor in waiting_queue:
        if str(visitor [0]) == search:
            print("Visitor Found Successfully!!")
            print("Token Number :",visitor[0])
            print("Visitor Name:", visitor[1])
            print("Service Type :", visitor[2])
            print("Waiting no.:",waiting_queue.index(visitor)+1)
            found = True
            break
    if found ==False:
        print("Visitor Not Found")
        print("".center(50,"-"))
