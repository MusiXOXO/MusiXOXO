import json
import requests



class easy_API :

    def get_auth_key(self):
        with open('AuthKey.txt') as read_file:
            return read_file.read()

    def get_artist_song(self, user_string ):
        artist_song = ['','']  #first goes artist then song name
        
        #find if its artist - song or just artist || also remove any spaces from front and back 
        if "-" in user_string:
            artist_song[0] = user_string[0: user_string.index('-') : 1].strip()
            artist_song[1] = user_string[user_string.index('-')+1 :  len(user_string)+1 : 1].strip()
        else:
            artist_song[0]=user_string

        #Get rid of needless 'spaces'
        artist_song[0].strip()
        return artist_song[0]

    def get_artist_id(self, name_of_artist) :
        
        url = f"https://api.spotify.com/v1/search?q={name_of_artist}&type=artist&limit=1"
        headers = {
            "Accept"        : "application/json",
            "Content-Type"  : "application/json",
        }

        headers['Authorization'] = f"Bearer {self.get_auth_key()}"
        myreq = requests.get(url, headers=headers)
        content = myreq.content
        status_code = myreq.status_code 
        if status_code != 200:
            print("Error: status code:", status_code)
            exit(-1)
        json_data = json.loads(content)

        items = json_data['artists']['items']
        for item in items:
            artist_id = item['id']
        
        return artist_id


    def get_track_id(self, name_of_track) :
        
        url = f"https://api.spotify.com/v1/search?q={name_of_track}&type=track&limit=1"
        headers = {
            "Accept"        : "application/json",
            "Content-Type"  : "application/json",
        }

        headers['Authorization'] = f"Bearer {self.get_auth_key()}"
        myreq = requests.get(url, headers=headers)
        content = myreq.content
        status_code = myreq.status_code 
        if status_code != 200:
            print("Error: status code:", status_code)
            exit(-1)
        json_data = json.loads(content)

        items = json_data['tracks']['items']
        for item in items:
            artist_id = item['id']
        
        return artist_id

    def get_recomendation(self, artist_id = None , song_id = None, limit=10) :
        url = f"https://api.spotify.com/v1/recommendations?limit={limit}"
        
        if artist_id != None:
            url +=f"&seed_artists={artist_id}"

        if song_id != None:
            url +=f"&seed_tracks={song_id}"

        headers = {
            "Accept"        : "application/json",
            "Content-Type"  : "application/json",
        }
        headers['Authorization'] = f"Bearer {self.get_auth_key()}"

        myreq = requests.get(url, headers=headers)
        content = myreq.content

        json_data = json.loads(content)
        
        recomendation_list = []

        for i in json_data['tracks']:
            
            data = {
                "song_name":{i['name']},
                "artist":{i['artists'][0]['name']},
                "link":{i['external_urls']['spotify']}
            }

            recomendation_list.append(data)  

        return recomendation_list
  
