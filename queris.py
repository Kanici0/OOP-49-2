CREATE_TABLE_registered = '''
    CREATE TABLE IF NOT EXISTS registered(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    age text,
    email text,
    city text,
    photo text,
    )
'''

INSERT_registered_query = '''
INSERT INTO registered(fullname, age, email, city, photo)
VALUES (?, ?, ?, ?, ?)
'''
