def generate_reports(waiting_queue):

    total_waiting = len(waiting_queue)
    total_served = len(completed_visitors)
    total_visitors = total_waiting + total_served

    print("\n========== QUEUE REPORT ==========")

    print("Total Visitors:", total_visitors)
    print("Visitors Waiting:", total_waiting)
    print("Visitors Served:", total_served)

    # Find the next visitor
    if waiting_queue:

        if priority_mode:
            next_visitor = get_next_visitor()
        else:
            next_visitor = waiting_queue[0]

        print("Next Token:", next_visitor["token"])

    else:
        print("Next Token: None")

    print("==================================")

    # Display completed visitor report
    print("\n------ SERVED VISITORS ------")

    if completed_visitors:

        for visitor in completed_visitors:
            print(
                visitor["token"],
                "-", visitor["name"],
                "-", visitor["service"]
            )

    else:
        print("No visitors have been served yet.")