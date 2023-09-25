from pathlib import Path

path = Path('guest.txt')

guest = input("What's your name? ")

path.write_text(guest)