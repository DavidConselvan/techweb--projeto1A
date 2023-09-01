import json
from database import Database
from database import Note   
db = Database('banco')

def extract_route(raw_request):
    lines = raw_request.splitlines()
    if len(lines) == 0:
        return None
    first = lines[0]

    path = first.split()[1]
    if path[0] == '/':
        path = path[1:]
    return path

def read_file(path):
    file = open(path,"r+b")
    return file.read()

def load_template(template):
    file = open("templates/"+ str(template), "r")
    return str(file.read())


def build_response(body = "", code = 200, reason = "OK", headers = ''):
    #status_line = f'HTTP/1.1 {code} {reason}'
    #response = f'{status_line}{headers}\n\n{body}'
    status_line = f'HTTP/1.1 {code} {reason}'
    if headers == '':
        response = f'{status_line}\n{headers}\n{body}'
    else:
        response = f'{status_line}\n{headers}\n\n{body}'
    
    return response.encode()