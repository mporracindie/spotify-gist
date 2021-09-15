import spotipy
from spotipy.oauth2 import SpotifyOAuth
from github import Github, InputFileContent
import os 

# export SPOTIPY_REDIRECT_URI='http://localhost'
# export SPOTIPY_CLIENT_ID=''
# export SPOTIPY_CLIENT_SECRET=''
# export GITHUB_ACCESS_TOKEN=''
gist_id = '5b7490ecfa945c45dd6dcd7f70896ca5'
gist_file_name = '🎵 My last week in music'

scope = "user-top-read"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

uset_top_artist = sp.current_user_top_artists(limit=5, offset=0, time_range='short_term')

lines = []
for i,artist in enumerate(uset_top_artist['items']):
    bar1 = ''.join(['████' for x in range(4-i)])
    bar2 = ''.join(['░░░░' for x in range(i)])
    lines.append(f"{i+1}. {artist['name']:20s} {bar1}{bar2} popularity: {artist['popularity']}\n")
    
g = Github(os.environ["GITHUB_ACCESS_TOKEN"])
file = {gist_file_name: InputFileContent(content=''.join(lines))}
gist = g.get_gist(gist_id).edit(files=file)