from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db


class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(
        db.String(80),
        unique=True,
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    stats = db.relationship(
        "UserStats",
        backref="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    attempts = db.relationship(
        "Attempt",
        backref="user",
        cascade="all, delete-orphan"
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(
            self.password_hash,
            password
        )

    def __repr__(self):
        return f"<User {self.username}>"


class UserStats(db.Model):
    __tablename__ = "user_stats"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        unique=True,
        nullable=False
    )

    games_played = db.Column(
        db.Integer,
        default=0
    )

    correct_answers = db.Column(
        db.Integer,
        default=0
    )

    wrong_answers = db.Column(
        db.Integer,
        default=0
    )

    total_score = db.Column(
        db.Integer,
        default=0
    )

    best_score = db.Column(
        db.Integer,
        default=0
    )

    @property
    def total_answers(self):
        return self.correct_answers + self.wrong_answers

    @property
    def accuracy(self):
        if self.total_answers == 0:
            return 0

        return round(
            self.correct_answers / self.total_answers * 100,
            2
        )

    def to_dict(self):
        """
        Diccionario dinámico para enviar las
        estadísticas a JavaScript.
        """

        return {
            "games_played": self.games_played,
            "correct_answers": self.correct_answers,
            "wrong_answers": self.wrong_answers,
            "total_score": self.total_score,
            "best_score": self.best_score,
            "accuracy": self.accuracy
        }


class Attempt(db.Model):
    __tablename__ = "attempts"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    target_country = db.Column(
        db.String(120),
        nullable=False
    )

    clicked_country = db.Column(
        db.String(120),
        nullable=False
    )

    correct = db.Column(
        db.Boolean,
        nullable=False
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )