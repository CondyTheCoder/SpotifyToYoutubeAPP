from flask import Flask, request, url_for, session, redirect
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

app.secret_key = "0:asdrxcASDfxz"

app.config['SESSION_COOKIE_NAME'] = 'Weiting Li'

@app.route('/')
def login():
    return 'Home'


@app.route('/redirect')
def redirect():
    return 'redirect'

@app.route('/getTracks')
def getTracks():
    return "Some random songs"

