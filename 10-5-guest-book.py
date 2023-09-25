from pathlib import Path

path = Path('guest_book.txt')
print("Enter 'quit' or 'q' when you are finished.")
while True:
    guest = input("\nWhat's your name? ")
    if guest == 'quit' or guest == 'q':
        break
    path.write_text(guest)
    print(f"Hi {guest}, you've been added to the guest book.")