import lyricsgenius
from retry import retry
import secrests



genius = lyricsgenius.Genius(secrests.GENIUS_ACCESS_CODE)


@retry(delay=5, tries=6)
def get_lyrics(artist,song):
    """Get song lyrics by artist name and song name from genius

    Args:
        artist (string): Artist name
        song (string): Song name

    Returns:
        string: The song lyrics or none if the song is not found
    """
    song = genius.search_song(song, artist)
    # song = artist.song(song_name)
    if song:
        return song.lyrics
    else:
        return None