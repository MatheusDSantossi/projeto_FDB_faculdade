from flask import logging

class User():
    def __init__(self, id, usuario, senha,nivel):
        self.id = id
        self.usuario = usuario
        self.senha = senha
        self.nivel = nivel

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def toJson(self):
        return dict(
            id=self.id,
            usuario=self.usuario,
            senha=self.senha,
            nivel=self.nivel,
        )