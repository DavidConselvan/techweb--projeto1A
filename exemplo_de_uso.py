from database import Database
from database import Note   
db = Database('banco')



notes = db.get_all()
for note in notes:
    print(f'Anotação {note.id}:\n  Título: {note.title}\n  Conteúdo: {note.content}\n')



db.delete('3')