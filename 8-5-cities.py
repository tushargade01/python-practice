def describe_city(city, country = 'india'):
    print(f'{city.title()} is in {country.title()}.')


describe_city('mumbai')
describe_city('punta arenas', 'chile')
describe_city('pune')