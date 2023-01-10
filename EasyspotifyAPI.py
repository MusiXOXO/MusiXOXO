import json
import requests
import pandas


class easy_API :

    def get_auth_key(self):
        with open('AuthKey.txt') as read_file:
            return read_file.read()

    def get_artist_song(self, user_string ):
        __artist_song = ['','']  #first goes artist then song name
        
        #find if its artist - song or just song || also remove any spaces from front and back 
        if "-" in user_string:
            __artist_song[0] = user_string[0: user_string.index('-') : 1].strip()
            __artist_song[1] = user_string[user_string.index('-')+1 :  len(user_string)+1 : 1].strip()
        else:
            __artist_song[1]=user_string

        #Get rid of needless 'spaces'
        __artist_song[0].strip()

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


test123 = easy_API()


print(test123.get_artist_id("Michael Ortega"))



    