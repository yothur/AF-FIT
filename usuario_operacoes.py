from flask import Flask, session

def is_authenticate():
    usuario = session.get("usuario_id")

    if usuario:
        return True
    return False