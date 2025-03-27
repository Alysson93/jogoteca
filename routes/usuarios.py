from jogoteca import app
from flask import session, flash, request, redirect, render_template
from models import Usuarios
from helpers import FormUsuario
from flask_bcrypt import check_password_hash


@app.route('/login', methods=['GET', 'POST'])
def login():
    proxima = request.args.get('proxima') or ''
    if 'usuario_logado' in session and session['usuario_logado'] != None:
        return redirect('/')
    if request.method == 'POST':
        form = FormUsuario(request.form)
        if not form.validate_on_submit():
            return redirect('/login')
        email = form.email.data
        usuario = Usuarios.query.filter_by(email=email).first()
        senha = check_password_hash(usuario.senha, form.senha.data)
        if usuario and senha:
            session['usuario_logado'] = request.form['nome']
            name = session['usuario_logado']
            flash(f'Usuário {name} logado com sucesso.', 'success')
            return redirect(f'/{proxima}')
        else:
            flash('Usuário não logado', 'danger')
            return redirect('/login')
    else:
        form = FormUsuario()
        return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Você saiu da sua conta com êxito', 'success')
    return redirect('/')