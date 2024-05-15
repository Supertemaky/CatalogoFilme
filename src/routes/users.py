from flask import Blueprint, render_template, request, redirect, url_for

user_route = Blueprint('user', __name__)

"""

##    ROTAS USUÁRIOS    ##

/user/ (GET) -- lista os usuários
/user/ (POST) -- inserir um novo usuário no banco de dados
/user/new/ (GET) -- exibe um formulario para a criação de um novo usuário
/users/<int:id> (GET) -- exibe dados de um usuário em específico
/users/<int:id>/edit/ (GET) -- exibe um formulário com os dados do usuário selecionado para editar
/users/<int:id>/update/ (PUT) -- envia uma atualização do usuário para o servidor
/users/<int:id>/delete/ (DELETE) -- deleta o usuário escolhido do servidor

"""

user_route.route('/')
def list_users():
 
    pass

user_route.route('/', methods=['POST'])
def insert_users():
 
    pass

user_route.route('/new')
def form_new_users():
 
    pass

user_route.route('/<int:user_id>')
def show_user():
 
    pass

user_route.route('/<int: user_id>/edit')
def form_edit_users():
 
    pass

user_route.route('/<int: user_id>/update', methods=['PUT'])
def update_user():
 
    pass

user_route.route('/<int: user_id>/delete', methods=['DELETE'])
def delete_user():
 
    pass
