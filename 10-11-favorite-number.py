from pathlib import Path
import json

f_number = input("Enter your favorite number: ")

path = Path('favorite.json')
content = json.dumps(f_number)
path.write_text(content)
