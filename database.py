import psycopg2 as db

host = 'localhost'
user = 'postgres'
password = 'LevRaven.1'
database = 'crud'
port = 5432


conn = db.connect(
    host=host,
    user=user,
    password=password,
    database=database,
    port=port
)

cur = conn.cursor()

# table creation
table_creation = '''
CREATE TABLE IF NOT EXISTS users(
id SERIAL PRIMARY KEY,
name VARCHAR(123),
email VARCHAR(123),
phone_number VARCHAR(123),
gender VARCHAR(6))'''

cur.execute(table_creation)
conn.commit()


# new user added
"""insert_user = '''INSERT INTO users (name, email, phone_number, gender)
VALUES ('Tom Hardy', '998998899889', 'tomhardy@gmail.com', 'male' )'''
cur.execute(insert_user)
conn.commit()"""


# A new user has been added and his gender is entered incorrectly because I want to update his gender
"""insert_user_for_update = '''
INSERT INTO users (name, email, phone_number, gender)
VALUES ('Mrs Wendy', '998998988998', 'wendy@gmail.com', 'male')'''
cur.execute(insert_user_for_update)
conn.commit()"""


# update table
"""
update_table = '''
UPDATE users SET gender = 'female' WHERE name = 'Mrs Wendy'
'''
cur.execute(update_table)
conn.commit()"""


# drop table
"""
drop_table = '''
DROP TABLE IF EXISTS users;'''
cur.execute(drop_table)
conn.commit()

"""
