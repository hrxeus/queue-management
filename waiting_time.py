def calculate_waiting_time(service_times, position):
    waiting_time = sum(service_times[:position - 1])
    return waiting_time


def waiting_time_simulation():

    print("----- Waiting Time Simulation -----")

    n = int(input("Enter number of visitors: "))

    waiting_queue = []

    for i in range(n):

        print("\nVisitor", i + 1)

        name = input("Enter visitor name: ")
        token = input("Enter token number: ")
        duration = int(input("Enter service time (minutes): "))

        visitor = {
            "name": name,
            "token": token,
            "duration": duration
        }

        waiting_queue.append(visitor)

    service_times = []

    for visitor in waiting_queue:
        service_times.append(visitor["duration"])

    print("\n----- Waiting Time Results -----")

    for i in range(len(waiting_queue)):

        visitor = waiting_queue[i]

        waiting_time = calculate_waiting_time(
            service_times, i + 1
        )

        print("\nVisitor:", visitor["name"])
        print("Token:", visitor["token"])
        print("Waiting Time:", waiting_time, "minutes")


waiting_time_simulation()     