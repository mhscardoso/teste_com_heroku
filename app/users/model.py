from app.extensions import db
from app.models import BaseModel
import bcrypt

class User(BaseModel):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False, unique=True, index=True)
    hash_pass = db.Column(db.LargeBinary, nullable=False)

    messages = db.relationship('Message', backref='user')

    @property
    def password(self):
        return AttributeError("Senha não é legível")
    
    @password.setter
    def password(self, new_pass):
        self.hash_pass = bcrypt.hashpw(new_pass.encode(), bcrypt.gensalt())