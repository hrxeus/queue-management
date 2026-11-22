def priority():
    for i in visitor:
        if i[2]=='Hall Ticket Issues':
            i.append(2)
        elif i[2]=='Fee Payment Enquiry':
            i.append(1)
        elif i[2]=='Admission Enquiry':
            i.append(3)
        elif i[2]=='Scholarship Assistance':
            i.append(4)

priority()
print(visitor)
visitor.sort(key=lambda x: x[-1])
print(visitor)
