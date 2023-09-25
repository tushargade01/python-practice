def make_car(manufacturer, model, **other_info):
    other_info['manufacturer'] = manufacturer
    other_info['model'] = model
    
    return other_info


car = make_car('subara','outback',color = 'black', year = '1989')
print(car)