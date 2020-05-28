import dbm
import json

DB_DEFAULTS=[
    {'dogs': 10, 'cats': 12},
    {'dogs': 2,  'cats': 11}
]

def db_init_defaults(some_db):
    for n,d in enumerate(DB_DEFAULTS):
        some_db[str(n)]=json.dumps(d)

def reset_db():
    with dbm.open('assets/test.db','c') as some_db:
        # initialize to defaults
        db_init_defaults(some_db)

if __name__ == "__main__":
    reset_db()
