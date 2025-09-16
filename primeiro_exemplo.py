from flask import *

#INSTANCIANDO O OBJETO DO SERVIDOR FLASK
app = Flask(__name__)

@app.route('/')
def abrir_home_page():
    return render_template('index.html')

@app.route('/fazerlogin', methods=['POST'])
def fazer_login():

    login = request.form.get('loginusuario')
    senha = request.form.get('senhausuario')

    if login == 'rene' and senha == '123':
        return render_template('logado.html')
    else:
        #aqui o usuario digitou o login ou senha errado
        msg = 'Usuário ou senha inválidos'
        return render_template('index.html', texto=msg)


@app.route('/logout')
def fazer_logout():
    return render_template('index.html')

#EXECUTANDO O SERVIDOR
app.run()