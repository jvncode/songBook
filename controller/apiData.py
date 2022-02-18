import requests
import json
from config import SHAZAM_HOST, SHAZAM_KEY, MUSIXMATCH_KEY, LASTFM_KEY, LASTFM_SECRET
from musixmatch import Musixmatch


class apiConnect:
    def __init__(self, query):
        self.query = query

    def getShazam(self):
        url = "https://shazam.p.rapidapi.com/search"

        querystring = {"term": self.query,
                       "locale": "es", "offset": "0", "limit": "15"}

        headers = {
            'x-rapidapi-host': SHAZAM_HOST,
            'x-rapidapi-key': SHAZAM_KEY
        }
        response = requests.request(
            "GET", url, headers=headers, params=querystring)
        return json.loads(response.text)

    def getMusixMatch(self):
        musixmatch = Musixmatch(MUSIXMATCH_KEY)
        musixmatch.chart_tracks_get(1, 1, f_has_lyrics=True)
        data = musixmatch.track_search(
            q_artist="", q_track=self.query, page_size=10, page=1, s_track_rating='desc')
        return data

    def getLastFM(self):
        url = 'https://ws.audioscrobbler.com/2.0/?method=track.search&track=' + \
            self.query + '&api_key=' + LASTFM_KEY + '&format=json'
        data = requests.get(url)
        return data.json()
