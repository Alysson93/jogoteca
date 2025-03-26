import os
from jogoteca import app
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField

class FormJogo(FlaskForm):
    nome = StringField('Nome do jogo', [validators.data_required(), validators.length(min=1, max=50)])
    categoria = StringField('Categoria do jogo', [validators.data_required(), validators.length(min=1, max=40)])
    console = StringField('Console do jogo', [validators.data_required(), validators.length(min=1, max=20)])
    salvar = SubmitField('Salvar')

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa_{id}' in nome_arquivo:
            return nome_arquivo
        else:
            return 'capa_default.jpg'


def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'capa_default.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))
