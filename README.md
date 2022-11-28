# Introduction

If you ever have a curiosity for music trends and lyrisc' sentiments, this dataset is for you. For this process, we collected the most popular songs on Spotify USA in the year 2021 and their lyrics. From Spotify API, we collected the songs' rankings, artists information, and some ranked features created by Spotify analysts. The lyrics part of the dataset is collected using Genius Open API. 

# Python packages used
lyricsgenius and spotify packages were used for this project

# API Access
In order to recreate the dataset on your own, make sure to request access from Spotify API and Genius API and change the credentials in the secrets.py prior to running the script. 

# Requirements
The codes are built on python 3.10.4
Code to install all the needed libraries for your convience

```pip install lyricsgenius pandas retry spotipy tqdm ```

# About the dataset
**track.csv**: Contains top 1000 popular songs on Spotify USA in 2021, with artist information and song attributes created by Spotify.
* artist_name: Artist's full name
* track_name: Track's full name
* track_id: Spotify track id
* track_popularity: Track's popularity scores on Spotify
* artist_id: Spotify artist id
* artist_followers: Number of artist's followers on Spotify
* artist_genres: Artist's track genres
* artist_popularity: Artist's popularity scores on Spotify
* Danceability: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
* Acousticness: A measure from 0.0 to 1.0 of whether the track is acoustic.
Energy: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy.
* Instrumentalness: Predicts whether a track contains no vocals. The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content.
* Liveness: Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live.
* Loudness: The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track. Values typical range between -60 and 0 db.
* Speechiness: Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value.
* Tempo: The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
* Valence: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).
* mode: Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0

**lyrics.csv**: Lyrics for the 1000 songs, collected from Genius API
* artist_name: The artist's full name
* track_name: The completed track name
* track_id: The track id by Spotify
* artist_id: The artist id by Spotify
* lyrics: The lyrics provides by Genius

# Inspiration
Some potential analysis you could do with this dataset:
1. NLP on song lyrics to extract sentiments and emotions of music during a time period.
2. Predict a song popularity based on features created by Spotify.
3. Find out what type of songs are more likely to be popular.

# References 
[Spotify API Documentation] <https://spotipy.readthedocs.io/en/master/>

[Get track features from Spotify] <https://developer.spotify.com/documentation/web-api/reference/#/operations/get-several-audio-features>

[Definition of track features] <https://medium.com/@boplantinga/what-do-spotifys-audio-features-tell-us-about-this-year-s-eurovision-song-contest-66ad188e112a#:~:text=Spotify>

[Genius API Documentation] <https://lyricsgenius.readthedocs.io/en/master/>

[Integration of Spotify and Genius API] <https://dev.to/willamesoares/how-to-integrate-spotify-and-genius-api-to-easily-crawl-song-lyrics-with-python-4o62>

[Genius API 101] <https://melaniewalsh.github.io/Intro-Cultural-Analytics/04-Data-Collection/07-Genius-API.html>
