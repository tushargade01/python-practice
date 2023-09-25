sandwich_orders = ['turkey sandwich','pastrami','roast beef sandwich','pastrami','grilled cheese sandwich','pastrami','veggie sandwich']
finished_sandwiches = []
while sandwich_orders:
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    sandwich = sandwich_orders.pop()
    print(f"I'm working on your {sandwich}")
    finished_sandwiches.append(sandwich)
print()    
for i in finished_sandwiches:
    print(f"I made a {i}")    
