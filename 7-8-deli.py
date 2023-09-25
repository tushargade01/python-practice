sandwich_orders = ['turkey sandwich','roast beef sandwich','grilled cheese sandwich','veggie sandwich']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I'm working on your {sandwich}")
    finished_sandwiches.append(sandwich)
print()    
for i in finished_sandwiches:
    print(f"I made a {i}")    
