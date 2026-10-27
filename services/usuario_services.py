from repository.usuariodao import UsuarioDAO
from modelos.usuario import Usuario


def cadastrar(nome, email):
    usuario = UsuarioDAO.buscar_por_email(email)
    if usuario:
        raise ValueError("Usuario Existente")
    return UsuarioDAO.salvar(Usuario(nome=nome, email=email))