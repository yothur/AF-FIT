from configdb import db
from modelos.usuario import Usuario

class UsuarioDao:
    @staticmethod
    def salvar(usuario):
        db.session.add(usuario)
        db.session.commit()

    @staticmethod
    def listar_Usuarios():
        return Usuario.query.all()

    @staticmethod
    def buscarPorEmail(email):
        return Usuario.query.filter_by(email=email).first()

    @staticmethod
    def remover(usuario):
        db.session.delete(usuario)
        db.session.commit()