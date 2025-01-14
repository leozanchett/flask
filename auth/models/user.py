from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    # role_id é uma coluna que armazena o ID do Role associado a este usuário
    # - db.Column() define uma coluna na tabela
    # - db.Integer especifica que é uma coluna de números inteiros
    # - db.ForeignKey('roles.id') cria uma chave estrangeira que referencia
    #   a coluna 'id' da tabela 'roles', estabelecendo o relacionamento
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

