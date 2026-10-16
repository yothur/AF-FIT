from flask import Blueprint, render_template, request, redirect, url_for, session
from usuario_operacoes import is_authenticate

from repository.usuariodao import UsuarioDAO

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def pagina_principal():
    if is_authenticate():
        return render_template('principal.html')
    return render_template('index.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if is_authenticate():
        return redirect(url_for('usuarios.pagina_inicial'))

    email = request.form.get('email').strip()
    senha = request.form.get('senha')

    usuario = UsuarioDAO.buscar_por_email(email)

    if usuario and usuario.senha == senha and usuario.is_admin:
        session['usuario_id'] = usuario.id
        return redirect(url_for('usuarios.pagina_inicial'))
    return render_template('index.html', mensagem='Erro ao fazer login'), 401

@auth_bp.route('/logout')
def logout():
    session.pop('usuario_id', None)
    return redirect(url_for('auth.pagina_principal'))