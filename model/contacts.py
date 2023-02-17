from model import connection

def all(cmd = "select * from tbl_contacts"):
    return [Contact(*i) for i in connection.cursor.execute(cmd).fetchall()]

class Contact :
    def __init__(self, id, name, fone, email):
        self.id = id
        self.name = name
        self.fone = fone
        self.email = email

def add(name, fone, email):
    connection.cursor.execute(f"insert into tbl_contacts (name, fone, email)  values ('{name}','{fone}','{email}')")

def get_by_id(id):
    args = connection.cursor.execute(f"select * from tbl_contacts where id = {id}").fetchone()
    return Contact(*args)

def update(id, name, fone, email):
    connection.cursor.execute(f"update tbl_contacts set name = '{name}', fone = '{fone}', email = '{email}' where id = {id}")

def delete(id):
    connection.cursor.execute("delete from tbl_contacts where id = {id}")

