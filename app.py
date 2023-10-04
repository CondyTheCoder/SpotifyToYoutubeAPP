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
TOKEN_INFO = "token_info"

@app.route('/')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/getTracks')
def getTracks():
    return "Some drake songs"

@app.route('/redirect')
def redirectPage():
    sp_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    session[TOKEN_INFO] = token_info

    return redirect(url_for('getTracks', _external= True))

def  create_spotify_oauth():
    return SpotifyOAuth(
        client_id = "c61a59ed39dc4628a7a2e22d3c76e5f7",
        client_secret = "525f9e7fd3c344d9b2a639add9445ca3",
        redirect_uri= url_for('redirectPage', _external= True),
        scope="user-library-read"
    )
