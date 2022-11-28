import json
def get_auth_key():
    with open('AuthKey.txt') as read_file:
        return read_file.read()

def get_artist_song( user_string ):
    __artist_song = ['','']  #first goes artist then song name
    
    #find if its artist - song or just song || also remove any spaces from front and back 
    if "-" in user_string:
        __artist_song[0] = user_string[0: user_string.index('-') : 1].strip()
        __artist_song[1] = user_string[user_string.index('-')+1 :  len(user_string)+1 : 1].strip()
    else:
        __artist_song[1]=user_string

    #Get rid of needless 'spaces'
    __artist_song[0].strip()

    return __artist_song