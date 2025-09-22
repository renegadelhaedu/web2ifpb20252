from flask import *
from utils.acesso import *

#INSTANCIANDO O OBJETO DO SERVIDOR FLASK
app = Flask(__name__)
usuarios = [['diego','d@d','123']]



@app.route('/')
def abrir_home_page():
    return render_template('index.html')

@app.route('/fazerlogin', methods=['POST'])
def fazer_login():

    login = request.form.get('loginusuario')
    senha = request.form.get('senhausuario')

    if verificar_login(usuarios, login, senha):
        return render_template('logado.html')
    else:
        #aqui o usuario digitou o login ou senha errado
        msg = 'Usuário ou senha inválidos'
        return render_template('index.html', texto=msg)


@app.route('/cadastrar', methods=['GET','POST'])
def cadastrar():
    if request.method == 'GET':
        return render_template('paginacadastro.html')

    nome = request.form.get('nomeuser')
    email = request.form.get('email')
    senha = request.form.get('senha')
    confirma = request.form.get('confirmacao')

    if senha == confirma:
        global usuarios
        usuarios.append([nome, email, senha])
        return render_template('index.html')
    else:
        msg = 'a senha e a confirmação de senha não são iguais'
        return render_template('paginacadastro.html', msg=msg)


@app.route('/logout')
def fazer_logout():
    return render_template('index.html')

#EXECUTANDO O SERVIDOR
app.run()