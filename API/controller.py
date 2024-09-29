from connection import Client

client = Client()

class Controller():
    def get_artist_controller(self,artist):
        results = client.sp.search(q='artist:' + artist, type='artist')
        items = results["artists"]["items"]
        if len(items) > 0:
            artist = items[0]
            return {"name" : artist["name"], "genres" : artist["genres"]}
    def get_track_controller(self,track):
        results = client.sp.search(q='track:' + track, type='track')
        items = results["tracks"]["items"]
        if len(items) > 0:
            track = items[0]
            return {"name": track['name'], "image" : track['album']["images"][2]["url"], "artist": track['album']["artists"][0]["name"]}