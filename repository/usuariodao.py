from configdb import db
from modelos.usuario import Usuario

class UsuarioDAO:
    @staticmethod
    def salvar(usuario):
        db.session.add(usuario)
        db.session.commit()

    @staticmethod
    def listar_usuarios():
        return Usuario.query.all()

    @staticmethod
    def buscar_por_email(email):
        return Usuario.query.filter_by(email=email).first()