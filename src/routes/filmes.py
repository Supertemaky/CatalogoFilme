from flask import Blueprint, render_template, request
from database.Models.filmes import Filmes

filme_route = Blueprint('filmes', __name__)

"""

##    ROTAS FILMES    ##

/filmes/ (GET) -- lista os filmes
/filmes/ (POST) -- inserir filmes no servidor
/filmes/new/ (GET) -- exibe um formulario para a adição de um novo filme
/filmes/<int:id> (GET) -- exibe dados de um filme em específico
/filmes/<int:id>/edit/ (GET) -- exibe um formulário com os dados do cliente selecionado para editar
/filmes/<int:id>/update/ (PUT) -- envia uma atualização do cliente para o servidor
/filmes/<int:id>/delete/ (DELETE) -- deleta o usuário escolhido do servidor


"""

@filme_route.route('/')
def listar_filmes():
    return render_template("listar_filmes.html")

@filme_route.route('/', methods=["POST"])
def inserir_filme():

    data = request.json

    novo_filme = Filmes.create(
        filme_nome = data['nomeFilme'],
        filme_data = data['dataLancamento'],
        filme_genero = data['generoFilme'],
        filme_duracao = data['duracaoFilme'],
        filme_sinopse = data['sinopseFilme'],
    )

    return render_template('listar_filmes.html', cliente = novo_filme)

@filme_route.route("/new")
def form_create_filme():
    return render_template("form_create_filme.html", methods=["POST"])

@filme_route.route("/<int:filme_id>")
def dados_filme():
    return render_template("dados_filme.html")

@filme_route.route("/<int:filme_id>/edit")
def form_editar_filme():
    return render_template("form_editar_filme.html")

@filme_route.route("/<int:filme_id>/update", methods=["PUT"])
def update_filme():
    return 'filme atualizado'

@filme_route.route("/<int:filme_id>/delete", methods=["DELETE"])
def delete_filme():
    return 'filme deletado'
