waiting_queue=["D","E","F","G"]
completed_queue=["A","B","C"]
def serve_visitor(waiting_queue,completed_queue):
    if len(waiting_queue)==0:
        print("No visitors left!!")
        return None
    current_visitor=waiting_queue[0]
    waiting_queue.pop(0)
    completed_queue.append(current_visitor)
    print("Served:",current_visitor)
    return current_visitor
serve_visitor(waiting_queue,completed_queue) 



