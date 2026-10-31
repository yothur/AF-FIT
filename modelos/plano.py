from datetime import datetime, timezone, timedelta
from configdb import db
import os

PLAN_EXPIRATION_TIME = int(os.getenv("PLAN_EXPIRATION_TIME"))

def calcular_vencimento():
    return datetime.now(timezone.utc) + timedelta(days=PLAN_EXPIRATION_TIME)

class Plano(db.Model):

    __tablename__ = "plano"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    escolha = db.Column(db.String(50), nullable=False)
    vencimento = db.Column(db.DateTime(timezone=True), nullable=False, default=calcular_vencimento)

    usuario = db.relationship("Usuario", backref=db.backref("plano", uselist=False), lazy=True)

    @property
    def is_expired(self):
        vencimento = self.vencimento
        return datetime.now(timezone.utc) >= vencimento

    def renew(self, escolha):
        self.escolha = escolha
        self.vencimento = datetime.now(timezone.utc) + timedelta(days=PLAN_EXPIRATION_TIME)