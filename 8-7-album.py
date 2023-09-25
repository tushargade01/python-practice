def make_album(title_name, artist_name, song_number = ''):
    album = {
        'title': title_name.title(),
        'artist': artist_name,
        'Song Number': song_number
    }
    print(album)


make_album('ninth symphony', 'beethoven')
make_album('ride the lighting', 'metallica', 9)
make_album('red-headed stranger', 'willie nelson')