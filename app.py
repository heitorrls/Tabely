from flask import Flask, render_template

# Inicializa a aplicação Flask
app = Flask(__name__)

# Rota para a página inicial (que será o Login)
@app.route('/')
def login():
    # O Flask procura automaticamente na pasta 'templates'
    return render_template('paginaLogin.html')

# Rota para a página de registo
@app.route('/cadastrese')
def cadastrese():
    return render_template('cadastrese.html')

# Rota para a aplicação principal (o reprodutor)
@app.route('/index')
def index():
    return render_template('index.html')

# Inicia o servidor em modo de depuração (debug)
if __name__ == '__main__':
    app.run(debug=True)