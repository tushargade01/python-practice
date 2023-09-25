def city_country(city, country = 'india'):
    return f'"{city.title()}", "{country.title()}"'
place = city_country('pune')    
print(place)
place = city_country('punta arenas', 'chile')    
print(place)
place = city_country('mumbai')    
print(place)