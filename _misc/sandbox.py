from dotenv import load_dotenv
import os
load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")

import sys
import spotipy
import spotipy.util as util

scope = 'user-library-read'
username = 'hotshot9258'
# if len(sys.argv) > 1:
#     username = sys.argv[1]
# else:
#     print("Usage: %s username" % (sys.argv[0],))
#     sys.exit()
print(SPOTIPY_REDIRECT_URI)
token = util.prompt_for_user_token(username, scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI, show_dialog=True)
if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_saved_tracks(limit=50)
    for item in results['items']:
        track = item['track']
        # print(track['name'] + ' - ' + track['artists'][0]['name'] + ', ID:')
else:
    print("Can't get token for", username)
    
    