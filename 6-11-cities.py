cities = {
    'kathmandu': {
        'country': 'nepal',
        'population': 1003285,
        'fact': 'The himalaya mountains are nearby'
    },
    'santiago': {
        'country': 'chile',
        'population': 6158080,
        'fact': 'The andes mountains are nearby'
    },
    'talkeetna': {
        'country': 'alaska',
        'population': 876,
        'fact': 'The alaska range mountains are nearby'
    }
}
for key,value in cities.items():
    print(f"{key.title()} is in {value['country'].title()}")
    print(f"\tit has a population of about {value['population']}")
    print(f"\t{value['fact']}")
