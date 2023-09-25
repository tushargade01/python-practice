peoples = {
    'shubham':[1,3],
    'vishal':[67,3],
    'tushar':[2,8],
    'karan':[9,1],
    'rushi':[12,53]
}
for key,value in peoples.items():
    print(f"{key} likes the following numbers:")
    for val in value:
        print(val)