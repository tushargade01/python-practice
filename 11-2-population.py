# def city_country(city,country,population):

#     all_data = f"{city}, {country} - {population}"
#     return all_data
    

def city_country(city,country,population = ''):
    if population:
        all_data = f"{city}, {country} - {population}"
    else:
        all_data = f"{city}, {country}."
    return all_data   

"""when you run this program please check file name that you import else you got a error"""