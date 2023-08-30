import json
from database import Database
from database import Note   
db = Database('banco')

def extract_route(string):
    new_string = string.split('\n')[0].split(' ')[1]
    new_string = new_string.replace('/', '',1)
    return new_string

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
    print("aqui --> ", response)
    return response.encode()