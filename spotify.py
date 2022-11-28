import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import secrests
import pandas as pd
from tqdm import tqdm
from retry import retry


client_credentials_manager = SpotifyClientCredentials(
    client_id=secrests.SPOTIFY_CLIENT_ID, client_secret=secrests.SPOTIFY_CLIENT_SECRET
)
sp_client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


@retry(delay=10, tries=3)
def require_popular_songs(year, number, step=50):
    """Request the popular songs from Spotify api with a given year

    Args:
        year (int): The year you want to search for
        number (int): Number of songs to search
        step (int, optional): The steps of query on the Spotify API. Defaults to 50.

    Returns:
        dataframe: The songs with artist and track name along with the popularity
    """
    artist_name = []
    track_name = []
    track_popularity = []
    artist_id = []
    track_id = []

    for i in tqdm(range(0, number, step)):
        track_results = sp_client.search(
            q=f"year:{year}", type="track", limit=step, offset=i
        )
        for i, t in enumerate(track_results["tracks"]["items"]):
            artist_name.append(t["artists"][0]["name"])
            artist_id.append(t["artists"][0]["id"])
            track_name.append(t["name"])
            track_id.append(t["id"])
            track_popularity.append(t["popularity"])

    df = pd.DataFrame(
        {
            "artist_name": artist_name,
            "track_name": track_name,
            "track_id": track_id,
            "track_popularity": track_popularity,
            "artist_id": artist_id,
        }
    )
    return df


@retry(delay=5, tries=6)
def request_single_artist_infomation(artist_id):
    """Request single artist infomation by artist id, will retry up to 6 times if there's some internet issue

    Args:
        artist_id (string): The artist id by Spotify

    Returns:
        dictionary: The artist informations provide by Spotify
    """
    return sp_client.artist(artist_id)


def assign_artist_info(df):
    """Assign the artist infomations to the track dataframe

    Args:
        df (dataframe): The original track dataframe containing the artist id

    Returns:
        dataframe: Updated dataframe containing artist information
    """
    artist_infos = []
    # get all unique artist informations
    for i in tqdm(df["artist_id"].unique()):
        artist = request_single_artist_infomation(i)
        if artist:
            artist_info = {
                "artist_id": artist["id"],
                "artist_followers": artist["followers"]["total"],
                "artist_genres": artist["genres"],
                "artist_popularity": artist["popularity"],
            }
            artist_infos.append(artist_info)
    df_artists = pd.DataFrame(artist_infos)
    # assign the new information back to origianl dataframe
    df = pd.merge(df, df_artists, how="left", on="artist_id")

    return df


@retry(delay=5, tries=6)
def request_single_audio_features(track_id):
    """Request single track features by artist id, will retry up to 6 times if there's some internet issue

    Args:
        track_id (string): The track id by Spotify

    Returns:
        dictionary: The song features provide by Spotify
    """
    return sp_client.audio_features(track_id)


def assign_track_features(df):
    """Assign the track features provided by Spotify to the track dataframe

    Args:
        df (dataframe): The original track dataframe containing the track id

    Returns:
        dataframe: Updated dataframe containing track features
    """
    track_features = []
    # get all track features
    for i in tqdm(df["track_id"]):
        audio_feature = request_single_audio_features(i)
        if audio_feature[0]:
            track_features.append(audio_feature[0])
    df_feature = pd.DataFrame(track_features)
    # drop unessary columns
    df_feature = df_feature.drop(
        ["type", "uri", "track_href", "analysis_url", "time_signature"], axis=1
    )
    df = pd.merge(df, df_feature, how="left", left_on="track_id", right_on="id")
    df = df.drop(["id"], axis=1)
    return df
