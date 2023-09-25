favorite_palces = []
place = {
    'name': 'anand',
    'place': ['mumbai','nagpur']
}
favorite_palces.append(place)

place = {
    'name': 'roshan',
    'place': ['pune','wednesday peth']
}
favorite_palces.append(place)

place = {
    'name': 'rohan',
    'place': ['karjat','nagar']
}
favorite_palces.append(place)
print(favorite_palces)

for item in favorite_palces:
    print(f"\n{item['name']} likes the following places:")
    for pal in item['place']:
        print(pal)
