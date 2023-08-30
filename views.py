from utils import load_template, build_response
import urllib.parse
from database import Database
from database import Note   
db = Database('banco')

def index(request):
    print( "request aqui -->", request, 'acabou')
    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados
        # Cabeçalho e corpo estão sempre separados por duas quebras de linha
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}
        # Preencha o dicionário params com as informações do corpo da requisição
        # O dicionário conterá dois valores, o título e a descrição.
        # Posteriormente pode ser interessante criar uma função que recebe a
        # requisição e devolve os parâmetros para desacoplar esta lógica.
        # Dica: use o método split da string e a função unquote_plus
        for chave_valor in corpo.split('&'):
            cv = urllib.parse.unquote_plus(chave_valor)
            if "titulo" in cv:
                params["titulo"] = cv[7:]
            if "detalhes" in cv:
                params['detalhes'] = cv[9:]
        new_note = Note(title = params['titulo'], content = params['detalhes'])
        db.add(new_note)
        return build_response(code = 303, reason = 'See Other', headers = 'Location: /')

    # O RESTO DO CÓDIGO DA FUNÇÃO index CONTINUA DAQUI PARA BAIXO...

    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title= dados.title, details = dados.content)
        for dados in db.get_all()
    ]
    notes = '\n'.join(notes_li)
    body = load_template('index.html').format(notes = notes)
    return build_response(body=body)