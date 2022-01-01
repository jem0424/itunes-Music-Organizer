from modules.my_library import MyLibrary


def write_songs_to_file(list):
    with open("Unused_Tracks_1.txt", "w") as file:
        for track in list:
            file.write(f"{track.name} {track.artist}\n")



# def comments(file):
#     audiofile = load("file:///Users/joelmunoz/Music/Music/Media.localized/Music/Dog%20Blood/Unknown%20Album/Middle%20Finger%202%20Vip.mp3")
#     print(f"# comments: {len(audiofile.tag.comments)}")
#     for comment in audiofile.tag.comments:
#         # Show comment
#         print(comment.description)
#         print(comment.text)
#         print(comment.lang)


if __name__ == '__main__':
    library = MyLibrary()
    tracks_not_in_playlists = library.find_songs_not_in_playlists()
    write_songs_to_file(tracks_not_in_playlists)
    # a = [song.comments() for song in songs_found_in_playlists]


