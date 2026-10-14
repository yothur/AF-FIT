from configdb import db

class Usuario(db.Model):

    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(150), nullable = False)
    email = db.Column(db.String(150), nullable = False) 
    senha = db.Column(db.String(255), nullable = True)
    tipo = db.Column(db.String(150), default = "usuario")

    @property
    def is_admin(self):
        self.tipo == "admin"