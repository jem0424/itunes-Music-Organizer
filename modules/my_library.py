from os import getenv
from os.path import join

from itunesLibrary.library import parse, Library

from modules.MySong import MySong


class MyLibrary(object):

    def __init__(self):
        self.music = self.load_itunes_library()
        self.custom_playlists = self.get_custom_playlists()

    @staticmethod
    def load_itunes_library():
        path = join(getenv("HOME"), "Music/iTunes/iTunes Media/Library.xml")
        return parse(path)

    def get_custom_playlists(self):
        playlists = [p for p in self.music.playlists if p.is_regular() is True]
        return playlists

    def get_playlist_by_track(self, track_id):
        matched_playlist = []
        for playlist in self.custom_playlists:
            playlist_track_ids = [track.itunesAttributes['Track ID'] for track in playlist.items]
            if track_id in playlist_track_ids:
                matched_playlist.append(playlist.title)
        return matched_playlist

    def get_tracks_in_current_playlists(self):
        songs = set()
        for playlist in self.custom_playlists:
            for item in playlist.items:
                songs.add(item)
        return list(songs)

    def find_songs_not_in_playlists(self):
        track_ids_in_playlists = [track.itunesAttributes['Track ID'] for track in self.get_tracks_in_current_playlists()]
        tracks_not_in_playlists = [MySong(item.itunesAttributes)
                                   for item in self.music.items
                                   if item.itunesAttributes['Track ID'] not in track_ids_in_playlists]
        return tracks_not_in_playlists

    def export_songs_not_in_playlists(self):
        track_ids_in_playlists = [track.itunesAttributes['Track ID'] for track in self.get_tracks_in_current_playlists()]
        tracks_not_in_playlists = [MySong(item)
                                   for item in self.music.items
                                   if item.itunesAttributes['Track ID'] not in track_ids_in_playlists]
        return tracks_not_in_playlists

class TestMyLibrary(Library):
    def __init__(self, ignoreRemoteSongs):
        super().__init__(ignoreRemoteSongs)