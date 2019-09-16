from itertools import combinations
from lemora import SQLiteKV
import hashlib
database = SQLiteKV.jsonDB( filename = "hashsha224.db")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,./\\~!@#$%^&*()_+*"
for x in range(1,5):
    comb = list(combinations(chars,x))
    for word in comb:
        word = "".join(word)
        print(word)
        database[hashlib.sha224(bytes(word,"UTF-8")).hexdigest()] = word[0]
database.commit()
database.close()
