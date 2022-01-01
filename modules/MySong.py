from urllib.parse import unquote
from os.path import isfile

from eyed3 import load


class MySong:
    def __init__(self, playlists=None, **kwargs, ):
        # self.attributes = attributes
        self.name = kwargs.get('Name', "")
        self.artist = kwargs.get('Artist', "")
        self.track_id = kwargs.get('Track_ID', 0)
        # self.comments = kwargs.get('Comments', "")
        self.matching_playlists = playlists
        self.file_location = self.normalize_file_path(kwargs.get("Location", ""))

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

    def __repr__(self):
        return f"{self.attributes}"

