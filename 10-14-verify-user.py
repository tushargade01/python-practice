from pathlib import Path
import json


def new_store(path):
    name = input("Whats your name? ")
    content = json.dumps(name)
    path.write_text(content)
    return content

def get_user(path):
    name = path.read_text()
    content = json.loads(name)
    return content

def greet_user():
    path = Path('verify_user.json')    
    if path.exists():
      user_name = get_user(path)
      ask = input(f"Are you {user_name}? (y/n) ")
      if ask == 'y' or ask == 'Y':
        print(f"Wlcome back, {user_name}!")
      elif ask == 'n' or ask == 'N':
        new_store(path)
    else:
        new_store(path)    

greet_user()    