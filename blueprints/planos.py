from flask import Blueprint, redirect, render_template, request, url_for, flash

from modelos.usuario import Usuario
from services.auth_services import is_authenticate
from services.plano_services import criar_plano, renovacao_plano, remocao_plano

planos_bp = Blueprint('planos', __name__, url_prefix='/planos')

@planos_bp.route('/')
def pagina_planos():
    if not is_authenticate():
        return redirect(url_for('auth.pagina_principal'))
    return render_template('planos.html')

@planos_bp.route('/novo/<int:usuario_id>', methods=['GET', 'POST'])
def novo_plano(usuario_id):
    if is_authenticate():
        if request.method == 'POST':
            try:
                criar_plano(usuario_id, request.form.get('escolha'))
                flash('Plano Cadastrado.', 'sucesso')
                return redirect(url_for('usuarios.pagina_inicial'))
            except ValueError as error:
                flash(str(error), 'erro')
                return render_template('novo_plano.html', usuario=Usuario.query.get(usuario_id))
        return render_template('novo_plano.html', usuario=Usuario.query.get(usuario_id))
    return render_template('index.html')


@planos_bp.route('/renovar/<int:usuario_id>', methods=['GET', 'POST'])
def renovar_plano(usuario_id):
    if is_authenticate():
        if request.method == 'POST':
            try:
                renovacao_plano(usuario_id, request.form.get('escolha'))
                flash('Plano Renovado!', 'sucesso')
                return redirect(url_for('usuarios.pagina_inicial'))
            except ValueError as error:
                flash(str(error), 'erro')
                return redirect(url_for('usuarios.pagina_inicial'))
        return render_template('novo_plano.html', usuario=Usuario.query.get(usuario_id))
    return render_template('index.html')


@planos_bp.route('/remover/<int:usuario_id>', methods=['GET', 'POST'])
def remover_plano(usuario_id):
    if is_authenticate():
        if request.method == 'POST':
            try:
                remocao_plano(usuario_id)
                flash('Plano removido!', 'sucesso')
            except ValueError as error:
                flash(str(error), 'erro')
        return redirect(url_for('usuarios.listarusuarios'))
    return render_template('index.html')