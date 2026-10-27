from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from services.auth_services import is_authenticate, logar

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
    try:
        logar(request.form.get('email').strip(), request.form.get('senha'))
        return redirect(url_for('usuarios.pagina_inicial'))
    except ValueError as error:
        flash(str(error), 'erro')
    return render_template('index.html')

@auth_bp.route('/logout')
def logout():
    session.pop('usuario_id', None)
    return redirect(url_for('auth.pagina_principal'))