def generate_reports(waiting_queue, completed_visitors):
    total_waiting = len(waiting_queue)
    total_served = len(completed_visitors)
    total_visitors = total_waiting + total_served
    print()
    print("[QUEUE REPORT]".center(50, "-"))
    print()
    print("Total Visitors:", total_visitors)
    print("Visitors Waiting:", total_waiting)
    print("Visitors Served:", total_served)

    if waiting_queue:
        print("Next Token to be Served:", waiting_queue[0][0])
    else:
        print("Next Token to be Served: None")

