from flask import Blueprint, render_template, request
from database.usuarios import USUARIOS


usuarios_route = Blueprint('usuarios', __name__)

#Rotas de usuários
# usuários/[GET] - listar os usuarios
# usuários/[POST] - inserir o usuario no servidor
# usuarios/new [GET] - renderizar o formulário para criar um usuário
# usuários/<id>[GET] - obter dados do usuario
# usuários/<id>/edit [GET] - renderiza um formulário para editar um usuário
# usuários/<id>/update [PUT] - atualizar os dados do usuário - cria um novo recurso (inclui) 
# ou substitui uma representação do recurso de destino pela carga útil da solicitação,
# usuários/<id>/delete [DELETE] - deleta o registro do usuário


#Vamos listar os usuarios nas rota principal de usuarios
@usuarios_route.route('/')
def listarUsuarios():
    return render_template('listaUsuarios.html', usuarios = USUARIOS)

@usuarios_route.route('/', methods = ['POST'])
def inserirUsuarios():
    dados = request.json
    novo_usuario ={
        "id":len(USUARIOS) + 1,
        "nome": dados['nome'],
        "email":dados['email'],
    }
    USUARIOS.append(novo_usuario)    
    return render_template('itemUsuario.html', usuario = novo_usuario)

@usuarios_route.route('/new', methods = ['GET'])
def formUsuarios():
    return render_template('formUsuario.html')

@usuarios_route.route('/<int:usuario_id>', methods = ['GET'])
def obterUsuarios(usuario_id):
    usuario = list(filter(lambda u: u['id'] == usuario_id, USUARIOS))[0]
    return render_template('obterUsuario.html', usuario=usuario)


@usuarios_route.route('/<int:usuario_id>/edit', methods = ['GET'])
def editarUsuarios(usuario_id):
    usuario = None
    for u in USUARIOS:
        if u['id'] == usuario_id:
            usuario = u
    return render_template('formUsuario.html', usuario=usuario)

@usuarios_route.route('/<int:usuario_id>/update', methods = ['PUT'])
def updateUsuarios(usuario_id):
    usuario_editado = None
    #obter dados do formulário de edição
    data = request.json
    #obter usuário pelo id
    for u in USUARIOS:
        if u['id'] == usuario_id:
            u['nome'] = data['nome']
            u['email'] = data['email']
            usuario_editado = u
    return render_template ('itemUsuario.html', usuario = usuario_editado)

@usuarios_route.route('/<int:usuario_id>/delete', methods = ['DELETE'])
def deletarUsuarios(usuario_id):
    global USUARIOS
    USUARIOS = [u for u in USUARIOS if u['id'] != usuario_id]
    return {'deleted': 'ok'}

