# JOGOTECA

Olá! Iniciando meus estudos em desenvolvimento web com Flask, e baseado nos cursos da plataforma Alura, desenvolvi um crud de jogos com autenticação, autorização e upload de imagens.


## Como rodar o projeto em sua máquina?

O único requisito é ter o python (3.10 ou maior) e o pip instalados. Caso queira criar um ambiente virtual para o projeto (recomendado se você não usar container), execute:

> python3 -m venv venv

Para acessar o ambiente virtual:
> source venv/bin/activate (Linux)
> venv\Scripts\activate (Windows)

Para instalar as dependências do projeto:
> pip install -r requirements.txt

Rode o projeto com:
> python jogoteca.py

Atenção: é no arquivo config.py que você irá configurar a string de conexão com o seu banco de dados. Certifique-se de ter um banco de dados que atenda as especificações dos models do projeto.