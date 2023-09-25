def make_album():
    while True:
        print("\nEnter 'quit' at any time to stop.\n")
        album_name = input("What album are you thinking of? ")
        if album_name == 'quit':
            break
        artist = input("Who's the artist? ")
        if artist == 'quit':
            break
        else:
            album = {
                'aritst': artist.title(),
                'title': album_name.title()
            }
        print(album) 

make_album()