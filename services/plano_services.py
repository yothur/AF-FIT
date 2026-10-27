from repository.planodao import PlanoDAO
from modelos.usuario import Usuario


def criar_plano(usuario_id, escolha):
    usuario = Usuario.query.get(usuario_id)
    if not usuario:
        raise ValueError('Usuário não existe!')
    if usuario.plano:
        raise ValueError('Usuário possui plano!')
    return PlanoDAO.salvar(usuario.id, escolha)

def renovacao_plano(usuario_id, escolha):
    usuario = Usuario.query.get(usuario_id)
    if not usuario:
        raise ValueError('Usuário não existe!')
    if not usuario.plano:
        raise ValueError('Usuário não possui plano!')
    if not usuario.plano.is_expired:
        raise ValueError('O plano do usuário não venceu!')
    return PlanoDAO.renovar_plano(usuario.id, escolha)

def remocao_plano(usuario_id):
    usuario = Usuario.query.get(usuario_id)
    if not usuario:
        raise ValueError('Usuário não existe!')
    if not usuario.plano:
        raise ValueError('Usuário não possui plano!')
    return PlanoDAO.remover(usuario_id)