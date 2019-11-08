#######
#Barebones SQLite
#######
import json
from sqlitedict import SqliteDict
def db(filename = "unnamed.sqlite"):
    return SqliteDict(filename)
def jsonDB(filename = "unnamed.sqlite"):
    return SqliteDict(filename, encode = json.dumps, decode = json.loads)
