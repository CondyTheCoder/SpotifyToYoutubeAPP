import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, url_for, session, request, redirect
import json
import time
import pandas as pd


# App config
app = Flask(__name__)

app.secret_key = 'SOMETHING YOU CAN THINK OF'
app.config['SESSION_COOKIE_NAME'] = 'spotify-login-name'

@app.route('/')
def login():
    return 'Jasons home page'

@app.route('/getTracks')
def getTracks():
    return "Some drake songs"

@app.route('/redirect')
def redirect():
    return 'redirect'

def  create_spotify_oauth():
    return SpotifyOAuth(
        client_id = "c61a59ed39dc4628a7a2e22d3c76e5f7",
        client_secret = "525f9e7fd3c344d9b2a639add9445ca3",
        redirect_uri= url_for('/redirect', _external=true),
        scope="user-library-read"
    )
