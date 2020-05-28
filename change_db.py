import dbm
import json

NEW_DB=[
    {'dogs': 100, 'cats': 102},
    {'dogs': -2,  'cats': 110}
]

def db_change(some_db):
    for n,d in enumerate(NEW_DB):
        some_db[str(n)]=json.dumps(d)

with dbm.open('assets/test.db','c') as some_db:
    db_change(some_db)
