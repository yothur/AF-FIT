from flask import Blueprint, redirect, render_template, request, url_for, flash

from modelos.usuario import Usuario
from repository.planodao import PlanoDAO
from usuario_operacoes import is_authenticate

planos_bp = Blueprint('planos', __name__, url_prefix='/planos')

@planos_bp.route('/')
def pagina_planos():
    if not is_authenticate():
        return redirect(url_for('auth.pagina_principal'))

    return render_template('planos.html')

@planos_bp.route('/novo/<int:usuario_id>', methods=['GET', 'POST'])
def novo_plano(usuario_id):
    if is_authenticate():
        usuario = Usuario.query.get(usuario_id)
        if request.method == 'POST':
            escolha = request.form.get('escolha')
            if not usuario:
                flash('Usuário não existe!', 'erro')
                return render_template('novo_plano.html', usuario=usuario)
            if usuario.plano:
                flash('Usuário já possui um plano!', 'erro')
                return render_template('novo_plano.html', usuario=usuario)

            PlanoDAO.salvar(usuario.id, escolha)
            flash('Plano Cadastrado.', 'sucesso')
            return redirect(url_for('usuarios.pagina_inicial'))
        return render_template('novo_plano.html', usuario=usuario)

    else:
        return render_template('index.html')


@planos_bp.route('/renovar/<int:usuario_id>', methods=['GET', 'POST'])
def renovar_plano(usuario_id):
    if is_authenticate():
        usuario = Usuario.query.get(usuario_id)
        if not usuario:
            flash('Usuário não existe!', 'erro')
            return render_template('principal.html'), 404
        if request.method == 'POST':
            escolha = request.form.get('escolha')
            if not usuario.plano:
                flash('Usuário não possui plano!', 'erro')
            elif usuario.plano.is_expired:
                if PlanoDAO.renovar_plano(usuario.id, escolha):
                    flash('Plano renovado!', 'sucesso')
                    return redirect(url_for('usuarios.pagina_inicial'))
                else:
                    flash('Erro ao renovar plano!', 'erro')
            else:
                flash('O plano ainda não venceu!', 'erro')

        return render_template('novo_plano.html', usuario=usuario)

    return render_template('index.html')


@planos_bp.route('/planos/remover/<int:usuario_id>', methods=['POST'])
def remover_plano(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if not usuario:
        flash('Usuário não existe!', 'erro')
        return redirect(url_for('usuarios.listarusuarios'))
    if not usuario.plano:
        flash('Usuário não possui plano!', 'erro')

    elif PlanoDAO.remover(usuario.id):
        flash('Plano removido!', 'sucesso')
    else:
        flash('Erro ao remover plano!', 'erro')
    return redirect(url_for('usuarios.listarusuarios'))