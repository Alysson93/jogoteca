from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'secret'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogos = [
    Jogo('Tetris', 'Puzzle', 'Atari'), 
    Jogo('God of War', 'Rack n Slash', 'PS2'), 
    Jogo('Super Mario', 'Plataforma', 'Nintendo'),
    Jogo('Mortal Kombat', 'Fight', 'PS2')
]

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

usuarios = [
    Usuario('Alysson', 'al@mail.com', '123'),
    Usuario('Pereira', 'pe@mail.com', '456'),
    Usuario('Assunção', 'as@mail.com', '789')
]
usuarios_dicionario = {usuario.email: usuario for usuario in usuarios}

@app.route('/')
def root():
    return render_template('lista.html', title='jogoteca', jogos=jogos)

@app.route('/novo', methods=['GET', 'POST'])
def novo():
    if 'usuario_logado' not in session or not session['usuario_logado']:
        flash('Você precisa estar logado para efetuar esta operação', 'danger')
        return redirect('/login?proxima=novo')
    if request.method == 'POST':
        nome = request.form['nome']
        categoria = request.form['categoria']
        console = request.form['console']
        jogos.append(Jogo(nome, categoria, console))
        flash('Jogo inserido com sucesso!', 'success')
        return redirect('/')
    else:
        return render_template('novo.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    proxima = request.args.get('proxima') or ''
    if request.method == 'POST':
        email = request.form['email']
        if email in usuarios_dicionario and request.form['senha'] == usuarios_dicionario[email].senha:
            session['usuario_logado'] = request.form['nome']
            name = session['usuario_logado']
            flash(f'Usuário {name} logado com sucesso.', 'success')
            return redirect(f'/{proxima}')
        else:
            flash('Usuário não logado', 'danger')
            return redirect('/login')
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Você saiu da sua conta com êxito', 'success')
    return redirect('/')

app.run(debug=True)