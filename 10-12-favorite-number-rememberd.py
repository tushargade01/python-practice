from pathlib import Path
import json

path = Path('user_favorite.json')

if path.exists():
    content = path.read_text()
    number = json.loads(content)
    print(f"I know your favorite number! It's {number}")
else:
    number = input("Enter your favorite number: ")
    content = json.dumps(number)
    path.write_text(content) 
