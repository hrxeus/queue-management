from add_new_visitor import completed_services


def serve_next_visitor(visitors):
    if not visitors:
        print("\nQueue is empty. No visitor to serve.")
        return

    visitor = visitors.pop(0)
    completed_services.append(visitor)
    token, name, service, priority = visitor

    print("\n----- Visitor Served -----")
    print("Token:", token)
    print("Name:", name)
    print("Service:", service)
