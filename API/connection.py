import spotipy
import os
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

load_dotenv()

class Client():
    def __init__(self):
        client_secret = os.getenv('SECRET_KEY')
        client_id = os.getenv('CLIENT_ID')
        manager = SpotifyClientCredentials(client_id, client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=manager)