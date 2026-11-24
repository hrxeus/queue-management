#Add visitor 
import random
token_number=[]
visitor_names=[]
service_types=[]
priority_level=[]

def unique_token_number():
    token 
    while True:
     token=random.randint(100,1000)
     if token not in token_number:
        token_number.append(token)
        return token 

def register_visitor():
    name=input("Enter visitor name:")
    service=input("Enter the type of service:")
    priority=input("Enter priority level:")
    token=unique_token_number()
    visitor_names.append(name)
    service_types.append(service)
    priority_level.append(priority)
    
    
    
    
    