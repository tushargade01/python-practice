from pathlib import Path

cat_path = Path('cats.txt')
dogs_path = Path('dogs.txt')


try:
    cat_content = cat_path.read_text()
except FileNotFoundError:
    pass
else:
    print(f"Reading File: {cat_path}")
    print(cat_content) 

print('')

try:
    dog_content = dogs_path.read_text()
except FileNotFoundError:
    pass
else:
    print(f"Reading File: {dogs_path}")
    print(dog_content)       
