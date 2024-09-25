#!/usr/bin/env python3

import json
import sys


try:
    db = json.load(open("db.json", "r"))
except:
    db = {}
    with open('db.json', 'w') as f:
        json.dump(db, f)
try:
    db[sys.argv[1]] = {"stalker": sys.argv[3], "username": sys.argv[2], "db": {}}
    json.dump(db, open("db.json", "w"))
    print("added user_id ", sys.argv[1], " with username ", sys.argv[2])
except:
    print("usage: add.py user_id username stalker_username", file=sys.stderr)
    exit(1)
