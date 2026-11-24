import add_new_visitor

def generate_reports(waiting_queue, completed_visitors):

    total_waiting = len(waiting_queue)
    total_served = len(completed_visitors)
    total_visitors = total_waiting + total_served

    print("\n========== QUEUE REPORT ==========")

    print("Total Visitors:", total_visitors)
    print("Visitors Waiting:", total_waiting)
    print("Visitors Served:", total_served)

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


def display_visitors(visitors, heading, empty_message):
    print(heading.center(50, "-"))
    if not visitors:
        print(empty_message)
        return

    for token, name, service, priority in visitors:
        print(f"Token {token} | {name} | {service} | Priority: {priority}")
