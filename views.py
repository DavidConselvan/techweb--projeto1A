from utils import load_template, build_response
import urllib.parse
from database import Database
from database import Note   
db = Database('banco')

def four_zero_four():
    body = load_template('four_zero_four.html')
    return build_response(body=body) 

def delete(id):
    id = str(id)
    db.delete(id)
    return build_response(code = 303, reason = 'See Other', headers = 'Location: /')

def index(request):
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        for chave_valor in corpo.split('&'):
            cv = urllib.parse.unquote_plus(chave_valor)
            if "titulo" in cv:
                params["titulo"] = cv[7:]
            if "detalhes" in cv:
                params['detalhes'] = cv[9:]
            if "id" in cv:
                params['id'] = cv[2:]
        
        new_note = Note(title = params['titulo'], content = params['detalhes'])
        db.add(new_note)
        
        return build_response(code = 303, reason = 'See Other', headers = 'Location: /')

    # O RESTO DO CÓDIGO DA FUNÇÃO index CONTINUA DAQUI PARA BAIXO...
    
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title= dados.title, details = dados.content, id = dados.id)
        for dados in db.get_all()
    ]
    notes = '\n'.join(notes_li)
    body = load_template('index.html').format(notes = notes)
    return build_response(body=body) 

def edit(request, id):
    note = db.get(id)
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        for chave_valor in corpo.split('&'):
            cv = urllib.parse.unquote_plus(chave_valor)
            if "titulo" in cv:
                params["titulo"] = cv[7:]
            if "detalhes" in cv:
                params['detalhes'] = cv[9:]
            if "id" in cv:
                params["id"] = cv[2:]
        
        note = Note(title = params['titulo'], content = params['detalhes'], id = id)
        db.update(note)
        return build_response(code = 303, reason = 'See Other', headers = 'Location: /')

    # O RESTO DO CÓDIGO DA FUNÇÃO index CONTINUA DAQUI PARA BAIXO...

    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title= dados.title, details = dados.content, id = note.id)
        for dados in db.get_all()
    ]
    notes = '\n'.join(notes_li)
    body = load_template('edit.html').format(titulo = note.title, conteudo = note.content)
    return build_response(body=body) 
