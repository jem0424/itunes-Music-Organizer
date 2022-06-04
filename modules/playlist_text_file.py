from modules.my_library import MyLibrary


class PlaylistTextFile:
    def __init__(self):
        self.headers = "Name\tArtist\tComposer\tAlbum\tGrouping\tWork\tMovement\tNumber\tMovement\tCount\tMovement\t" \
                       "Name\tGenre\tSize\tTime\tDisc\tNumber\tDisc\tCount\tTrack\tNumber\tTrack\tCount\tYear\tDate\t" \
                       "Modified\tDate\tAdded\tBit\tRate\tSample\tRate\tVolume\tAdjustment\tKind\tEqualizer\t" \
                       "Comments\tPlays\tLast\tPlayed\tSkips\tLast\tSkipped\tLocation"

    def write_songs_to_file(self, tracks: list):
        with open("Unused Tracks Playlist.txt", "w") as file:
            file.write(self.headers)
            for track in tracks:
                file.write(f"{track.metadata} {track.artist}\n")


if __name__ == '__main__':
    playlist = PlaylistTextFile()
    library = MyLibrary()
    tracks_not_in_playlists = library.export_songs_not_in_playlists()
    # TODO Add Song Serializer for text file
    playlist.write_songs_to_file(tracks_not_in_playlists)