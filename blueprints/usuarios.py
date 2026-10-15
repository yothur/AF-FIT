from flask import Blueprint, render_template, request
from usuario_operacoes import is_authenticate

from modelos.usuario import Usuario
from repository.usuariodao import UsuarioDAO

usuarios_bp = Blueprint('usuarios', __name__)


@usuarios_bp.route('/principal')
def pagina_inicial():
    return render_template('principal.html')

@usuarios_bp.route('/cadastrarusuario', methods=['GET', 'POST'])
def cadastrarusuario():
    if is_authenticate():
        if request.method == 'GET':
            return render_template('cadastrarusuario.html')

        nome = request.form.get('nome')
        email = request.form.get('email')

        usuario = UsuarioDAO.buscar_por_email(email)

        if usuario:
            return render_template('cadastrarusuario.html', mensagem='Usuario Existente!'), 401

        UsuarioDAO.salvar(Usuario(nome=nome, email=email))

        msg = "Usuário Cadastrado!"
    else:
        msg = "Erro no Cadastro!"

    return render_template('principal.html', msg=msg)

@usuarios_bp.route('/listarusuarios')
def listarusuarios():
    return render_template('listarusuarios.html', usuarios=UsuarioDAO.listar_usuarios())