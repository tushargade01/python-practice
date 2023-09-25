from pathlib import Path
import json

def get_stored_user(path):
    user_info = path.read_text()
    content = json.loads(user_info)
    return content

def new_user(path):
    user_all_data = {}
    user_name = input("Whats your name: ")
    fav_game = input("What's your favorite game? ")
    fav_animal = input("What's your favorite animal? ")
    user_all_data['name'] = user_name
    user_all_data['game'] = fav_game
    user_all_data['animal'] = fav_animal
    content = json.dumps(user_all_data)
    path.write_text(content)
    
    return user_all_data

def user():
    path = Path('user_info.json')
    if path.exists():
        userinfo = get_stored_user(path)
        print(f"Wlcome back, {userinfo['name']}!")
        print(f"Hope you've been playing some {userinfo['game']}.")
        print(f"have you seen a {userinfo['animal']} recently?.")
    else:
        userinfo = new_user(path)  

user()              