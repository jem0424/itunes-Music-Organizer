from modules.my_library import MyLibrary

import csv


def write_songs_to_file(tracks: list):
    with open("Unused_Tracks.txt", "w") as file:
        for track in tracks:
            file.write(f"{track.name} {track.artist}\n")


def write_to_csv(tracks: list):
    with open("unused_tracks.csv", "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=";")
        for track in tracks:
            csv_writer.writerow([f"{track.name}; {(track.artist if track.artist else 'N/A')}; {track.file_location}"])


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
    write_to_csv(tracks_not_in_playlists)
    # a = [song.comments() for song in songs_found_in_playlists]
