import sqlite3
from os import path

local_path = path.dirname(path.realpath(__file__))

connection = sqlite3.Connection(path.join(local_path, "datasource.bd"), check_same_thread=False)

cursor = connection.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS tbl_contacts(
        id integer primary key,
        name text not null,
        fone text,
        email text
    )
 ''')