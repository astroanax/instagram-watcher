import json

settings = json.load(open("settings.json", "r"))
class relation:
    def __init__(self, t, user_id, username):
        self.type = t
        self.URL = "https://www.instagram.com/api/v1/friendships/" + user_id + "/" + t + "/?count=12"
        self.headers = {
                'authority': 'www.instagram.com',
                'accept': '*/*', 
                'accept-language': 'en-US,en;q=0.9', 
                'referer': 'https://www.instagram.com/' + username + '/'+ t + '/',
                'x-requested-with': 'XMLHttpRequest',
                'cookie': settings['cookie'],
                'x-asbd-id':settings['x-asbd-id'], 
                'x-csrftoken': settings['x-csrftoken'],
                'x-ig-app-id': settings['x-ig-app-id'],
                'x-ig-www-claim': settings['x-ig-www-claim'],
                }

class followers(relation):
    def __init__(self, user_id, username):
        super().__init__("followers", user_id, username)
class following(relation):
    def __init__(self, user_id, username):
        super().__init__("following", user_id, username)
