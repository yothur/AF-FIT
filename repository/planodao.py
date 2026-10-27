from configdb import db
from modelos.plano import Plano

class PlanoDAO:
    @staticmethod
    def salvar(id, escolha):
        db.session.add(Plano(usuario_id=id, escolha=escolha))
        db.session.commit()

    @staticmethod
    def renovar_plano(id, escolha):
        plano = Plano.query.filter_by(usuario_id=id).first()
        plano.renew(escolha)
        db.session.commit()

    @staticmethod
    def remover(id):
        plano = Plano.query.filter_by(usuario_id=id).first()
        db.session.delete(plano)
        db.session.commit()