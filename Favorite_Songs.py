def favorite_songs(playlist):
    playlist.sort(key = lambda song: song["plays"], reverse = True)
    first_song = playlist[0]["title"]
    second_song = playlist[1]["title"]

    return [first_song, second_song]