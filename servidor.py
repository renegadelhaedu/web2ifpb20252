from flask import *

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/enviar', methods=['POST'])
def receber_mensagem():
    login = request.form.get('login')
    senha = request.form.get('senha')
    if login == 'admin' and senha == '123':
        msg = 'vc esta logado'
        return render_template('retorno.html', msg =msg)
    else:
        return render_template('index.html')



app.run(host='0.0.0.0', port=80)