from flask import Blueprint, render_template, request, flash
from services.auth_services import is_authenticate
from services.usuario_services import cadastrar

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
        try:
            cadastrar(request.form.get('nome'), request.form.get('email'))
            return render_template('principal.html', msg="Usuário Cadastrado!")
        except ValueError as error:
            flash(str(error), 'erro')
            return render_template('principal.html')
    else:
        return render_template("index.html")

@usuarios_bp.route('/listarusuarios')
def listarusuarios():
    return render_template('listarusuarios.html', usuarios=UsuarioDAO.listar_usuarios())