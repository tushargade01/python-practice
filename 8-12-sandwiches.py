def sandwich(*requred):
    print("\nI'll make a great sandwich:")
    for requre in requred:
        print(f"\t....adding {requre} to your sandwich.")
        
    print('Your sandwich is ready!')    

sandwich('roast beef','cheddar cheese','lettuce','honey dijon')

sandwich('turkey','apple slices','honey muatard')

sandwich('peanut butter','strawberry jam')
