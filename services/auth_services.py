from flask import session

from repository.usuariodao import UsuarioDAO

def is_authenticate():
    usuario = session.get("usuario_id")

    if usuario:
        return True
    return False

def logar(email, senha):
    usuario = UsuarioDAO.buscar_por_email(email)
    if not usuario:
        raise ValueError("Erro ao fazer login")
    elif usuario.senha == senha and usuario.is_admin:
        session['usuario_id'] = usuario.id
    else:
        raise ValueError("Erro ao fazer login")
    return usuario.id