import sqlite3

class DbHelper:
    def __init__(self,dbname='todoI.sqlite'):
        #initialize like constructor
        #by default store data in todo.sqlite db and create connection
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        #creates new table called items in db, with one column description
        #table - items, column - description, text -datatype
        stmt = 'CREATE TABLE IF NOT EXISTS items (description text, owner text)'
        self.conn.execute(stmt)
        self.conn.commit()

    def add_item(self,item_text,owner):
        #inserts given item in table
        stmt = 'INSERT INTO items (description, owner) VALUES (?,?)'
        args = (item_text, owner)
        self.conn.execute(stmt,args)
        self.conn.commit()

    def delete_item(self,item_text,owner):
        #deletes the item from table
        stmt = 'DELETE FROM items where description = (?) AND owner = (?)'
        args = (item_text,owner)
        self.conn.execute(stmt,args)
        self.conn.commit()

    def get_items(self,owner):
        #returns list of all items in tuple format,
        #only x[0] i.e., first item is displayed
        stmt = 'SELECT description FROM items WHERE owner = (?)'
        args = (owner, )
        return [x[0] for x in self.conn.execute(stmt,args)]
