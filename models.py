from jogoteca import db

class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Nome: %r' % self.nome


class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Nome: %r' % self.nome