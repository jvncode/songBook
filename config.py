import os
from dotenv import load_dotenv
load_dotenv()


# API SHAZAM
SHAZAM_HOST = os.getenv('SHAZAM_HOST', default='')
SHAZAM_KEY = os.getenv('SHAZAM_KEY', default='')

# API MUSIXMATCH
MUSIXMATCH_KEY = os.getenv('MUSIXMATCH_KEY', default='')

# API LASTFM
LASTFM_KEY = os.getenv('LASTFM_KEY', default='')
LASTFM_SECRET = os.getenv('LASTFM_SECRET', default='')
