import requests
import json
import json
import logging
import relations
import copy

try:
    logging.basicConfig(
        filename="watcher.log",
        filemode='a',
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.INFO
        )
except:
    with open('watcher.log', 'w') as f:
        f.write('')

try:
    db = json.load(open('db.json', 'r'))
except:
    db = {}
    with open('db.json', 'w') as f:
        json.dump(db, f)

def fetch(relation, URL, headers, db, username):
    if not relation in db:
        db[relation] = {}
    response = None
    users = {}
    while response is None or "next_max_id" in response:
        if response is not None:
            max_id = "&max_id=" + response["next_max_id"]
        else: max_id = ""
        r = requests.get(URL + max_id, headers=headers)
        response = json.loads(r.text)
        for user in response['users']:
            users[user["pk_id"]] = {"name": user["full_name"], "username": user["username"]}
            if not user["pk_id"] in db[relation]:
                db[relation][user["pk_id"]] = {"name": user["full_name"], "username": user["username"]}
                logging.info("new " + relation + " - " + user["full_name"] + " - " + user["username"] + " for " + username)
            else:
                if user["username"] != db[relation][user["pk_id"]]["username"]:
                    db[relation][user["pk_id"]]["username"] = user["username"]
                if user["full_name"] != db[relation][user["pk_id"]]["name"]:
                    db[relation][user["pk_id"]]["name"] = user["full_name"]

    db1 = copy.deepcopy(db)
    for user in db1[relation]:
        if user not in users:
            logging.info("removed " + relation + " - " + db1[relation][user]["name"] + " - " + db1[relation][user]["username"] + " for " + username)
            del db[relation][user]
    return db


for user_id in db:
    username = db[user_id]["username"]
    user_db = db[user_id]["db"]
    followers = relations.followers(user_id, username)
    following = relations.following(user_id, username)
    user_db = fetch(followers.type, followers.URL, followers.headers, user_db, username)
    user_db = fetch(following.type, following.URL, following.headers, user_db, username)
    db[user_id]["db"] = user_db


json.dump(db, open('db.json', 'w'))
