import json

class relation:
    def __init__(self, t, user_id, username, headers):
        self.type = t
        self.URL = "https://www.instagram.com/api/v1/friendships/" + user_id + "/" + t + "/?count=12"
        self.headers = headers
        self.headers.update({
                'authority': 'www.instagram.com',
                'accept': '*/*', 
                'accept-language': 'en-US,en;q=0.9', 
                'referer': 'https://www.instagram.com/' + username + '/'+ t + '/',
                'x-requested-with': 'XMLHttpRequest',
                })

class followers(relation):
    def __init__(self, user_id, username, headers):
        super().__init__("followers", user_id, username, headers)
class following(relation):
    def __init__(self, user_id, username, headers):
        super().__init__("following", user_id, username, headers)
