completed_services = []

def serve_next_visitor(visitors):
    if not visitors:
        print("Queue is empty. No visitor to serve.")
        print()
        return

    visitor = visitors.pop(0)
    completed_services.append(visitor)
    token, name, service, priority = visitor

    print()
    print("[VISITOR SERVED]".center(50, "-"))
    print("Token:", token)
    print("Name:", name)
    print("Service:", service)
    print("-" * 50)
    print()
