from flask import *
produtos = [['lapis','3.80','serve pra pintar', 'd@d'],['cadeira','45.80','serve pra sentar', 'camila@jesus.com']]


produto_bp = Blueprint('produto', __name__, url_prefix='/produto')


@produto_bp.route('/cadastrarproduto', methods=['GET','POST'])
def cadastrar_produto():
    if 'login' not in session:
        return render_template('index.html')

    if request.method == 'GET':
        return render_template('produto/cadastroproduto.html')

    nome = request.form.get('nome')
    preco = request.form.get('preco')
    descricao = request.form.get('descricao')
    produtos.append([nome, preco, descricao, session['login']])
    print(produtos)
    return render_template('logado.html')


@produto_bp.route('/listarmeusprodutos')
def listar_meus_produtos():
    if 'login' not in session:
        return render_template('index.html')

    lista_produtos = []
    for produto in produtos:
        if produto[3] == session['login']:
            lista_produtos.append(produto)

    return render_template('produto/listarmeusprodutos.html', lista=lista_produtos)


