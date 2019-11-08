#######
#Barebones SQLite
#######
import json,bz2,sqlite3
from sqlitedict import SqliteDict
def encode(data):
    return sqlite3.Binary(bz2.compress(json.dumps(data).encode()))
def decode(data):
    return json.loads(bz2.decompress(data).decode())
def db(filename = "unnamed.sqlite"):
    return SqliteDict(filename, encode = encode, decode = decode)
