# Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title, num_of_songs=None):
    if num_of_songs:
        return {'artist_name': f'{artist_name}',
                'album_title': f'{album_title}',
                'num_of_songs': num_of_songs
                }
    else:
        return {'artist_name': f'{artist_name}',
                'album_title': f'{album_title}'
                }

while True:
    print('Enter "q" at any time to quit.')

    artist = input('Name of the Artist: ')
    if artist == 'q':
        break

    album = input('Name of the Album: ')
    if album == 'q':
        break

    print(make_album(artist, album))


