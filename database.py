import sqlite3
from dataclasses import dataclass

@dataclass
class Database:
    def __init__(self,db_name):
        self.conn = sqlite3.connect(db_name + '.db')
        self.conn.execute(f"CREATE TABLE IF NOT EXISTS note ( id INTEGER PRIMARY KEY, title STRING, content STRING NOT NULL);")
    
    def add(self, note):
         self.conn.execute(f"INSERT INTO note (title, content) VALUES ('{note.title}', '{note.content}');")
         self.conn.commit()

    def get_all(self):
        notes = []
        print(notes)
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content= linha[2]
            new_note = Note(id,title,content)
            notes.append(new_note)
        return notes
    
    def update(self, entry):
        sql = "UPDATE note SET title = ?, content = ? WHERE id = ?"
        args = (entry.title, entry.content,entry.id)
        self.conn.execute(sql,args)
        self.conn.commit()

    def delete(self, note_id):
        sql = "DELETE FROM note WHERE id = ?;"
        args = (note_id)
        self.conn.execute(sql,args)
        self.conn.commit()  

@dataclass
class Note:
    id:int = None
    title: str = None
    content: str = ''


    