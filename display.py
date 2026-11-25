def display_visitors(visitors, heading):
    print()
    print(f"[{heading}]".center(50, "-"))
    if not visitors:
        print("No visitor here")
        print()
        return

    for token, name, service, priority in visitors:
        print(f"{token} | {name} | {service} | Priority: {priority}")
    print("-" * 50)
    print()
