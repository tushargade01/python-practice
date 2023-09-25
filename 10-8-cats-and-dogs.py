from pathlib import Path

cats_path = Path('cats.txt')
dogs_path = Path('dogs.txt')

print(f"Reading File: {cats_path}") #print file name by assigned word.
try:
    cats_content = cats_path.read_text() #read files and store into cats & dogs content
except FileNotFoundError:
    print("Sorry, I cant't find that file.")    
else:
    print(cats_content)

    print('')

print(f"Reading File: {dogs_path}")
try:
    dogs_content = dogs_path.read_text()
except FileNotFoundError:
    print("Sorry, I cant't find that file.")        
else:    
    print(dogs_content)