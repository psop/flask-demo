from .. import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), primary_key=True)
    email = db.Column(db.String(120), primary_key=True)

def _create(username, email):
    user = User(id=1, username = username, email = email)
    db.session.add(user)
    db.session.commit()
    return