from urllib.parse import unquote
from os.path import isfile

from eyed3 import load


class MySong:
    def __init__(self, attributes, playlists=None):
        self.metadata = attributes
        self.track_id = self.metadata.get("Track ID", "")
        self.name = self.metadata.get("Name", "")
        self.artist = self.metadata.get("Artist", "")
        self.genre = self.metadata.get("Genre", "")
        self.kind = self.metadata.get("Kind", "")
        self.size = self.metadata.get("Size", "")
        self.total_time = self.metadata.get("Total Time", "")
        self.bpm = self.metadata.get("BPM", "")
        self.grouping = self.metadata.get("Grouping", "")
        self.work = self.metadata.get("Work", "")
        self.movement = self.metadata.get("Movement", "")
        self.date_modified = self.metadata.get("Date Modified", "")
        self.date_added = self.metadata.get("Date Added", "")
        self.bit_rate = self.metadata.get("Bit Rate", "")
        self.sample_rate = self.metadata.get("Sample Rate", "")
        self.volume_adjustment = self.metadata.get('Volume Adjustment', "")
        self.comments = self.metadata.get('Comments', "")
        self.normalization = self.metadata.get('Normalization', "")
        self.persistent_id = self.metadata.get('Persistent ID', "")
        self.track_type = self.metadata.get('Track Type', "")
        self.raw_location = self.metadata.get("Location", "")
        self.movement_number = self.metadata.get("Movement Number", "")
        self.movement_count = self.metadata.get("Movement Count", "")
        self.movement_name = self.metadata.get("Movement Name", "")
        self.disc_number = self.metadata.get("Disc Number", "")
        self.disc_count = self.metadata.get("Disc Count", "")
        self.track_number = self.metadata.get("Track Number", "")
        self.track_count = self.metadata.get("Track Count", "")
        self.year = self.metadata.get("Year", "")
        self.equalizer = self.metadata.get("Equalizer", "")
        self.plays = self.metadata.get("Plays", "")
        self.last_played = self.metadata.get("Last Played", "")
        self.skips = self.metadata.get("Skips", "")
        self.last_skipped = self.metadata.get("Last Skipped", "")
        self.composer = self.metadata.get("Composer", "")
        self.album = self.metadata.get("Album", "")
        self.file_location = self.normalize_file_path(self.raw_location)
        self.matching_playlists = playlists

    @staticmethod
    def normalize_file_path(file_path):
        new_path = unquote(file_path)
        return new_path.replace("file://", "")

    def comments(self):
        if isfile(self.file_location):
            audiofile = load(self.file_location)
            print(audiofile)
            # if audiofile and audiofile.tag.comments:
            #     print(f"# comments: {len(audiofile.tag.comments)}")
            #     for comment in audiofile.tag.comments:
            #         # Show comment
            #         print(comment.description)
            #         print(comment.text)
                    # print(comment.lang)
        # Remove comment. Doesn't work with empty descriptions.
        # audiofile.tag.comments.remove(comment.description)
        # print(f"# comments (after remove): {len(audiofile.tag.comments)}")
        # audiofile.tag.save()

    def find_key(self):
        pass

    def serialize(self):
        return f"{self.name}\t{self.artist}\t{self.composer}\t{self.album}\t{self.grouping}\t{self.work}\t" \
               f"{self.movement_number}\t{self.movement_count}\t{self.movement_name}\t{self.genre}\t{self.size}\t" \
               f"{self.total_time}\t{self.disc_number}\t{self.disc_count}\t{self.track_number}\t{self.track_count}\t" \
               f"{self.year}\t{self.date_modified}\t{self.date_added}\t{self.bit_rate}\t{self.sample_rate}\t" \
               f"{self.volume_adjustment}\t{self.kind}\t{self.equalizer}\t{self.comments}\t{self.plays}\t" \
               f"{self.last_played}\t{self.skips}\t{self.last_skipped}\t{self.file_location}\n"

    def __repr__(self):
        return f"{self.name}, {self.artist}, {self.file_location}"

