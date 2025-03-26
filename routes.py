from flask import send_from_directory, render_template, request, redirect, session, flash
from jogoteca import app, db
from models import Usuarios, Jogos
from config import UPLOAD_PATH
from helpers import recupera_imagem, deleta_arquivo, FormJogo
import time

@app.route('/')
def root():
    jogos = Jogos.query.order_by(Jogos.id)
    return render_template('lista.html', title='jogoteca', jogos=jogos)

@app.route('/novo', methods=['GET', 'POST'])
def novo():
    if 'usuario_logado' not in session or not session['usuario_logado']:
        flash('Você precisa estar logado para efetuar esta operação', 'danger')
        return redirect('/login?proxima=novo')
    if request.method == 'POST':
        form = FormJogo(request.form)
        if not form.validate_on_submit():
            return redirect('/novo')
        jogo = Jogos(
            nome=form.nome.data,
            categoria=form.categoria.data,
            console=form.console.data
        )
        db.session.add(jogo)
        db.session.commit()
        imagem = request.files['imagem']
        timestamp = time.time()
        imagem.save(f'{UPLOAD_PATH}/capa_{jogo.id}-{timestamp}.jpg')
        flash(f'Jogo adicionado com sucesso.', 'success')
        return redirect('/')
    else:
        form = FormJogo()
        return render_template('novo.html', form=form)


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id: int):
    if 'usuario_logado' not in session or not session['usuario_logado']:
        flash('Você precisa estar logado para efetuar esta operação', 'danger')
        return redirect(f'/login?proxima=editar/{id}')
    jogo = Jogos.query.filter_by(id = id).first()
    if not jogo:
        return redirect('/')
    capa_jogo = recupera_imagem(id)
    if request.method == 'POST':
        form = FormJogo(request.form)
        if not form.validate_on_submit():
            return redirect(f'/editar/{id}')
        jogo.nome = form.nome.data
        jogo.categoria = form.categoria.data
        jogo.console = form.console.data
        db.session.commit()
        imagem = request.files['imagem']
        timestamp = time.time()
        deleta_arquivo(jogo.id)
        imagem.save(f'{UPLOAD_PATH}/capa_{jogo.id}-{timestamp}.jpg')
        flash(f'Jogo editado com sucesso.', 'success')
        return redirect('/')
    else:
        form = FormJogo(request.form)
        return render_template('editar.html', jogo=jogo, capa_jogo=capa_jogo, form=form)


@app.route('/deletar/<int:id>', methods=['POST'])
def deletar(id: int):
    if 'usuario_logado' not in session or not session['usuario_logado']:
        flash('Você precisa estar logado para efetuar esta operação', 'danger')
        return redirect('/')
    jogo = Jogos.query.filter_by(id = id).first()
    if not jogo:
        return redirect('/')
    db.session.delete(jogo)
    db.session.commit()
    flash(f'Jogo deletado com sucesso.', 'success')
    return redirect('/')


@app.route('/login', methods=['GET', 'POST'])
def login():
    proxima = request.args.get('proxima') or ''
    if 'usuario_logado' in session and session['usuario_logado'] != None:
        return redirect('/')
    if request.method == 'POST':
        email = request.form['email']
        usuario = Usuarios.query.filter_by(email=email).first()
        if usuario and request.form['senha'] == usuario.senha:
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


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)
