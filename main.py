import os
from itunesLibrary import library

if __name__ == '__main__':

    path = os.path.join(os.getenv("HOME"), "Music/iTunes/iTunes Music Library.xml")

    # must first parse...
    lib = library.parse(path)

    print(len(lib))  # number of items stored

    for playlist in lib.playlists:
        for item in playlist.items:
            print(item)  # perform function on each item in the playlist

    # get a single playlist
    playlist = lib.getPlaylist("Gray")

    # check the playlist type
    assert (not playlist.is_smart())
    assert (not playlist.is_folder())

    # get a list of all of the David Bowie songs
    bowie_items = lib.getItemsForArtist("David Bowie")

    # get a single song
    single_song = lib.getItemsById("16116")

    # get the iTunes application version
    print(lib.applicationVersion)
    # print(count)
    # print(f"Enter Token: {argv[1]}")
    # spotify= SpotifyClient(argv[1])
    # spotify.check_profile()
    # spotify.get_liked_tracks()

#     trackID=trackrow.text
#     props = trackrow.findall('*')
#     #name = trackrow.find('string').text
#     fields = trackrow.findall('key')
#     name = fields[1].text
#     trackname = trackrow.findall('string')[0].text
#     artist = fields[2].text
#     artisttext = trackrow.findall('string')[1].text
#     album = fields[3].text
#     albumtext = trackrow.findall('string')[2].text
#     genre = fields[4].text
#     genretext = trackrow.findall('string')[3].text
#     filetype= fields[5].text
#     filetypetext = trackrow.findall('string')[4].text
#     size = fields[6].text
#     sizenum = trackrow.findall('integer')[1].text
#     time = fields[7].text
#     tracktime = trackrow.findall('integer')[2].text
#     year = fields[8].text
#     trackyear = trackrow.findall('integer')[3].text
#     bpmfield = fields[9].text
#     bpm = trackrow.findall('integer')[4].text
#     datemodfield = fields[10].text
#     datemod = trackrow.findall('date')[0].text
#     dateaddfield = fields[11].text
#     dateadd = trackrow.findall('date')[1].text
#     bitratefield = fields[12].text
#     bitrate = trackrow.findall('integer')[5].text
#     commentfield = fields[14].text
#     comments = trackrow.findall('string')[5].text
#     #unplayedfield = fields[21].text
#     #unplayedflag =
#     locationfield = fields[22].text
#     location = trackrow.findall('string')[9].text
#     filefoldercount = fields[23].text
#     ffcount = trackrow.findall('integer')[9].text
#
#     #This will find text for the
#     print(ffcount)
#
"""     vclient = MongoClient('localhost',27017)
        db=vclient.myDB
        result = db.data.insert_one({name:trackTitle})
        print (result.inserted_id) 
"""
