login = 'maria'
senha = '1234'
usuario_encontrado = False

usuarios = [
    {"login": "admin", "senha": "1234", "permissao": "admin"},
    {"login": "gernte", "senha": "abcd", "permissao": "gerente"},
    {"login": "vendedor", "senha": "asdf", "permissao": "vendedor"},
    {"login": "joao", "senha": "1234", "permissao": "admin"},
    {"login": "maria", "senha": "abcd", "permissao": "genrente"},
    {"login": "thiago", "senha": "asdf", "permissao": "vendedor"}
]

for ususario in usuarios:
    if(login == ususario ['login'] and senha == ususario['senha']):
        print(ususario['permissao'])
        usuario_encontrado = False
        break
    if not usuario_encontrado:
        print('Usuario não encontrado')