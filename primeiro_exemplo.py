from flask import *
from utils.acesso import *
from blueprints.produto_bp import produto_bp
from dao.banco import init_db, Session
from dao.usuarioDAO import *

#INSTANCIANDO O OBJETO DO SERVIDOR FLASK
app = Flask(__name__)
app.secret_key = 'HGF431kSD&'

usuarios = None

app.register_blueprint(produto_bp)
#criando a estrutura do banco de dados, caso nao tenha sido criado antes
#init_db()

@app.before_request
def pegar_sessao():
    g.session = Session()

@app.teardown_appcontext
def encerrar_sessao(exception=None):
    Session.remove()

@app.route('/')
def abrir_home_page():
    return render_template('index.html')

@app.route('/fazerlogin', methods=['POST', 'GET'])
def fazer_login():

    if request.method == 'GET' and 'login' in session:
        return render_template('logado.html')

    login = request.form.get('loginusuario')
    senha = request.form.get('senhausuario')

    usuario_dao = UsuarioDAO(g.session)

    #if verificar_login(usuarios, login, senha):
    usuario = usuario_dao.autenticar(login, senha)
    if usuario:
        print(usuario)
        session['login'] = login
        return render_template('logado.html')
    else:
        #aqui o usuario digitou o login ou senha errado
        msg = 'Usuário ou senha inválidos'
        return render_template('index.html', texto=msg)


@app.route('/cadastrar', methods=['GET','POST'])
def cadastrar():
    if request.method == 'GET':
        return render_template('paginacadastro.html')

    usuario_dao = UsuarioDAO(g.session)

    nome = request.form.get('nomeuser')
    email = request.form.get('email')
    senha = request.form.get('senha')
    confirma = request.form.get('confirmacao')

    if senha == confirma:
        novo_usuario = Usuario(email=email, nome=nome, senha=senha)
        usuario_dao.criar(novo_usuario)
        return render_template('index.html')
    else:
        msg = 'a senha e a confirmação de senha não são iguais'
        return render_template('paginacadastro.html', msg=msg)


@app.route('/listar')
def listar_usuarios():
    if 'login' in session:

        usuarioDAO = UsuarioDAO(g.session)

        usuarios_lista = usuarioDAO.listar_usuarios()

        return render_template('listar.html',usuarios=usuarios_lista)
    else:
        return render_template('index.html')

@app.route('/detalhes')
def mostrar_detalhes():

    email = request.values.get('email')
    usuario = buscar_usuario(usuarios, email) #simulando um banco de dados

    if usuario:
        return render_template('detalhes.html', usuario=usuario)
    msg = 'usuário nao encontrado'
    return render_template('mensagemerro.html', msg=msg)

#end-point ou route (rota)
@app.route('/dados')
def pegar_dados():
    id = request.values.get('id')
    nome_user = request.values.get('nome')
    if id:
        print(id)
    if nome_user:
        print(nome_user)
    return 'deu cerrtooo'


@app.route('/logout')
def fazer_logout():
    #limpo o objeto session (dicionário)
    session.clear()
    return render_template('index.html')

#EXECUTANDO O SERVIDOR
app.run()